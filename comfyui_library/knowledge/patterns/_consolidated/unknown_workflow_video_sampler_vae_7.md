---
name: unknown_workflow_video_sampler_vae_7
type: Unknown Workflow
frequency: 34
level: moderate
coverage: 0.989412
common_nodes: [LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1936085964831772673.json, 视频生成/图生视频/1936088683596648450.json, 视频生成/图生视频/1936098801763405825.json, 视频生成/图生视频/1937498299152646145.json, 视频生成/图生视频/2072861939096702977.json, 视频生成/图生视频/2029023080860884994.json, 视频生成/图生视频/1932593243689263106.json, 视频生成/图生视频/1935907722095157250.json, 视频生成/图生视频/1963139208418406401.json, 视频生成/图生视频/2067073325549051906.json, 视频生成/图生视频/2067543097009070082.json, 视频生成/图生视频/2069607660957298690.json, 视频生成/图生视频/2071484855296286721.json, 视频生成/图生视频/2075211940145754113.json, 视频生成/图生视频/2075529541229039617.json, 视频生成/图生视频/2075529801041014786.json, 视频生成/图生视频/2076596033949360129.json, 视频生成/图生视频/2076614896099352578.json, 视频生成/图生视频/2077671450340839425.json, 视频生成/图生视频/2080534588438441986.json, 视频生成/图生视频/1995763601367502849.json, 视频生成/图生视频/2032000865069961218.json, 视频生成/图生视频/2035963740117540866.json, 视频生成/图生视频/1900406595552014337.json, 视频生成/文生视频/1935508018886791169.json, 视频生成/文生视频/1949634225363918849.json, 视频生成/文生视频/1940219782467862530.json, 视频生成/文生视频/1943534867973873665.json, 视频生成/文生视频/1937316067234758658.json, 视频生成/文生视频/1935860061073760257.json, 视频生成/文生视频/1948914179688865793.json, 视频生成/文生视频/1938411233160921090.json, 视频生成/文生视频/1918486985445675009.json, 视频生成/文生视频/1928319038026596353.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_vae_7

> 由 `engine/knowledge_consolidation` 从 34 个 workflow 归纳得出（视频生成/图生视频/1936085964831772673.json、视频生成/图生视频/1936088683596648450.json、视频生成/图生视频/1936098801763405825.json、视频生成/图生视频/1937498299152646145.json、视频生成/图生视频/2072861939096702977.json…）

- **类型**：Unknown Workflow
- **样本数**：34
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 34 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `ImageResizeKJ` —— 33/34 个有
- `WanVideoClipVisionEncode` —— 33/34 个有
- `WanVideoImageToVideoEncode` —— 33/34 个有
- `WanVideoLoraSelect` —— 33/34 个有
- `WanVideoTorchCompileSettings` —— 30/34 个有
- `CLIPVisionLoader` —— 28/34 个有
- `Primitive integer [Crystools]` —— 27/34 个有
- `Text Multiline` —— 27/34 个有
- `WanVideoVACEModelSelect` —— 26/34 个有
- `LoadWanVideoClipTextEncoder` —— 6/34 个有
- `Text` —— 3/34 个有
- `WanVideoSLG` —— 2/34 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/34 个有
- `GIMMVFI_interpolate` —— 1/34 个有
- `WanVideoImageClipEncode` —— 1/34 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
