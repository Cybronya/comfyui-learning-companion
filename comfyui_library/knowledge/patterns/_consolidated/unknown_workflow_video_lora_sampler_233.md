---
name: unknown_workflow_video_lora_sampler_233
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 1
common_nodes: [ImageScaleToTotalPixels, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader, easy imageSize]
problems: []
missing: []
members: [视频生成/图生视频/1910865402451427330.json, 视频生成/图生视频/1926200490214780930.json, 视频生成/图生视频/1932016531797159938.json, 视频生成/文生视频/1950803002250698754.json, 视频生成/文生视频/1951208338203848706.json, 视频生成/文生视频/1960218004153905154.json, 视频生成/文生视频/1942781187436032002.json, 视频生成/文生视频/1943248788255629314.json, 视频生成/文生视频/1943678559179378689.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_233

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/1910865402451427330.json、视频生成/图生视频/1926200490214780930.json、视频生成/图生视频/1932016531797159938.json、视频生成/文生视频/1950803002250698754.json、视频生成/文生视频/1951208338203848706.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 9 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy imageSize`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: PurgeVRAM V2` —— 8/9 个有
- `RH_Captioner` —— 7/9 个有
- `easy cleanGpuUsed` —— 7/9 个有
- `Replace Text _O` —— 2/9 个有
- `ImageBatch` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `Primitive string [Crystools]` —— 1/9 个有
- `RunningHub_UNO_Loadmodel` —— 1/9 个有
- `RunningHub_UNO_Sampler` —— 1/9 个有
- `SaveImage` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
