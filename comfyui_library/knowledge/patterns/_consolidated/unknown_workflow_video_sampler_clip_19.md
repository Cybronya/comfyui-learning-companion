---
name: unknown_workflow_video_sampler_clip_19
type: Unknown Workflow
frequency: 18
level: moderate
coverage: 0.967556
common_nodes: [LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1955497685786791938.json, 视频生成/图生视频/1985661621626384386.json, 视频生成/图生视频/1990706310121480193.json, 视频生成/图生视频/产品360度旋转工作流_2107332312026411009.json, 视频生成/图生视频/2019717359677739009.json, 视频生成/图生视频/1900164696572571649.json, 视频生成/图生视频/2036986018880036866.json, 视频生成/图生视频/1940589072328929281.json, 视频生成/图生视频/1947139195913154561.json, 视频生成/图生视频/2004811036769349634.json, 视频生成/图生视频/1998646989552279553.json, 视频生成/图生视频/2066782224497860610.json, 视频生成/图生视频/1923645906959462401.json, 视频生成/图生视频/1923299741252112385.json, 视频生成/图生视频/1923617442441195522.json, 视频生成/图生视频/1939900014733004802.json, 视频生成/文生视频/1922456339556028417.json, 视频生成/文生视频/1930515723595190274.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_19

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（视频生成/图生视频/1955497685786791938.json、视频生成/图生视频/1985661621626384386.json、视频生成/图生视频/1990706310121480193.json、视频生成/图生视频/产品360度旋转工作流_2107332312026411009.json、视频生成/图生视频/2019717359677739009.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：中等可信
- **平均知识覆盖**：97%

## 共有节点

全部 18 个 workflow 都包含：
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoLoraSelect` —— 17/18 个有
- `WanVideoExperimentalArgs` —— 16/18 个有
- `WanVideoSLG` —— 16/18 个有
- `easy cleanGpuUsed` —— 13/18 个有
- `FILM VFI` —— 12/18 个有
- `ImageUpscaleWithModel` —— 12/18 个有
- `Upscale Model Loader` —— 12/18 个有
- `ImageResizeKJ` —— 11/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/18 个有
- `Text` —— 3/18 个有
- `Int` —— 2/18 个有
- `TextInput_` —— 2/18 个有
- `Fast Groups Bypasser (rgthree)` —— 1/18 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
