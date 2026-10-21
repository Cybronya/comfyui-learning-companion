---
name: unknown_workflow_video_upscale_lora_3
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.947583
common_nodes: [ImageUpscaleWithModel, LayerUtility: PurgeVRAM, LoadImage, LoadWanVideoClipTextEncoder, LoadWanVideoT5TextEncoder, UpscaleModelLoader, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEnhanceAVideo, WanVideoImageClipEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTeaCache, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1896816638631550978.json, 视频生成/图生视频/1903839569089826817.json, 视频生成/图生视频/1899415692570181634.json, 视频生成/图生视频/1899312280767516673.json, 视频生成/图生视频/1900467836874301442.json, 视频生成/图生视频/1899699069881860097.json, 视频生成/图生视频/2005178859836370946.json, 视频生成/图生视频/1899713009114107905.json, 视频生成/图生视频/1894935249389039617.json, 视频生成/图生视频/1932255495774437378.json, 视频生成/图生视频/1930816773925306370.json, 视频生成/文生视频/1904728293755813889.json]
source: knowledge_consolidation
---

# unknown_workflow_video_upscale_lora_3

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/1896816638631550978.json、视频生成/图生视频/1903839569089826817.json、视频生成/图生视频/1899415692570181634.json、视频生成/图生视频/1899312280767516673.json、视频生成/图生视频/1900467836874301442.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 12 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoadWanVideoClipTextEncoder`
- `LoadWanVideoT5TextEncoder`
- `UpscaleModelLoader`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEnhanceAVideo`
- `WanVideoImageClipEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTeaCache`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoTorchCompileSettings` —— 9/12 个有
- `Int` —— 7/12 个有
- `RIFE VFI` —— 7/12 个有
- `ImageResizeAdvanced` —— 5/12 个有
- `Note Plus (mtb)` —— 4/12 个有
- `Fast Groups Bypasser (rgthree)` —— 2/12 个有
- `Text Multiline` —— 2/12 个有
- `TextInput_` —— 2/12 个有
- `WanVideoEmptyEmbeds` —— 2/12 个有
- `WanVideoSLG` —— 2/12 个有
- `ImageResizeKJ` —— 1/12 个有
- `ResizeLongestToNode` —— 1/12 个有
- `SaveLatent` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
