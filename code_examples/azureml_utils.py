import os

from azureml.core import Workspace,Dataset
from azureml.core.authentication import ServicePrincipalAuthentication
from azureml.core.compute import ComputeTarget, AmlCompute


def get_workspace():
    '''
    This function gets the ML workspace by using service principle.

    Returns
    -------
    ws : TYPE
        DESCRIPTION.

    '''
    svc_pr = ServicePrincipalAuthentication(
        tenant_id=os.getenv("ws_tenant_id"),
        service_principal_id=os.getenv("ws_app_id"),
        service_principal_password=os.getenv("ws_secret")
        )
    ws = Workspace(
        subscription_id=os.getenv("subscription_id"),
        resource_group=os.getenv("resource_group"),
        workspace_name=os.getenv("ws_name"),
        auth=svc_pr
        )
    return ws

def get_compute_target(ws, cluster_name="rcluster", vm_size = "STANDARD_D2_V2"):
    '''
    This function create/use the the available cluster.

    Parameters
    ----------
    ws : TYPE
        DESCRIPTION.
    cluster_name : TYPE, optional
        DESCRIPTION. The default is "rcluster".
    vm_size : TYPE, optional
        DESCRIPTION. The default is "STANDARD_D2_V2".

    Returns
    -------
    compute_target : TYPE
        DESCRIPTION.

    '''
    if (cluster_name in ws.compute_targets):
        compute_target = ws.compute_targets[cluster_name]
        if compute_target and type(compute_target) is AmlCompute:
            print('Found compute target: ' + cluster_name)
    else:
        print('Creating a new compute target...')
        provisioning_config = AmlCompute.provisioning_configuration(vm_size=vm_size,
                                                                    min_nodes=1,
                                                                    max_nodes=2)
        # create the compute target
        compute_target = ComputeTarget.create(
            ws, cluster_name, provisioning_config)
        # Can poll for a minimum number of nodes and for a specific timeout.
        # If no min node count is provided it will use the scale settings for the cluster
        compute_target.wait_for_completion(
            show_output=True, min_node_count=None, timeout_in_minutes=20)
        # For a more detailed view of current cluster status, use the 'status' property
        print(compute_target.status.serialize())
    return compute_target
