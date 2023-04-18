<img src="https://user-images.githubusercontent.com/8587189/232764837-40865915-1cef-40da-989b-f19773b15de1.png" align="right" width="75" height="75">

# colab-tunnel

Access Google Colab directly from your local VS Code editor using [remote tunnels](https://code.visualstudio.com/docs/remote/tunnels).

https://user-images.githubusercontent.com/8587189/232783372-8f2a5f83-1e57-42f0-8740-4b7e5901b561.mp4

## Usage
You can make a copy of this [notebook](https://colab.research.google.com/drive/1VAlrgB4IpBazkQRrZtSPjeTNR3P27FwQ?usp=sharing) to get started.

On Google Colab, first install the library and the run the code.
```shell
!pip install colabtunnel
```

```python
from colabtunnel import colabtunnel

colabtunnel()
```

1. After running the code, copy the given code, click the GitHub link and paste the code.
<p align="center">
<img width="965" alt="image" src="https://user-images.githubusercontent.com/8587189/232768841-fbd2e1bd-91d1-49ac-989e-277e50604209.png">
</p>

2. Paste your unique code on the github link and press "Continue".
<p align="center">
<img width="516" alt="image" src="https://user-images.githubusercontent.com/8587189/232766772-effe800b-4184-42ac-b03d-4810ce072428.png">
</p>

3. Open your local VSCode Editor. Install the [Remote Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server) extension if you haven't already installed. Then, open the command prompt and select **Remote-Tunnels: Connect to Tunnel**
<p align="center">
<img width="747" alt="image" src="https://user-images.githubusercontent.com/8587189/232767017-65ef61c4-99bc-48a1-be1d-88ad47b6d595.png">
</p>

4. You will be shown a list of tunnels. Select the first tunnel name that has **online** beside it.
<p align="center">
<img width="676" alt="image" src="https://user-images.githubusercontent.com/8587189/232767113-b7acac1c-c236-4dcb-852c-fbe179e3e6ab.png">
</p>

5. You will be connected to the virtual machine and can access the folders. Open the `/colab` folder and store your code there for persistence on Google Drive. The workflow is similar to the Remote SSH plugin

![image](https://user-images.githubusercontent.com/8587189/232769273-52d3e26a-3aec-436d-9b60-97e1d190ddf7.png)

