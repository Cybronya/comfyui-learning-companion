---
name: unknown_workflow_video_lora_sampler_549
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.84875
common_nodes: [CreateCFGScheduleFloatList, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1952588298072068097.json, 视频生成/文生视频/(6+6)Wan2.2 Smooth Mix高动态文生视频(KJ版)_1978740744045400065.json, 视频生成/文生视频/1961658398267916290.json, 视频生成/文生视频/1950046289267441666.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_549

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/1952588298072068097.json、视频生成/文生视频/(6+6)Wan2.2 Smooth Mix高动态文生视频(KJ版)_1978740744045400065.json、视频生成/文生视频/1961658398267916290.json、视频生成/文生视频/1950046289267441666.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：85%

## 共有节点

全部 4 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 3/4 个有
- `GetImageSizeAndCount` —— 3/4 个有
- `LayerUtility: PurgeVRAM` —— 3/4 个有
- `ImageFromBatch+` —— 2/4 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/4 个有
- `LoadImage` —— 2/4 个有
- `WanVideoEmptyEmbeds` —— 2/4 个有
- `WanVideoImageToVideoEncode` —— 2/4 个有
- `AILab_MiniCPM_4_V` —— 1/4 个有
- `LoadLatent` —— 1/4 个有
- `LoadVideo` —— 1/4 个有
- `SaveImage` —— 1/4 个有
- `SaveLatent` —— 1/4 个有
- `VHS_LoadVideoFFmpeg` —— 1/4 个有
- `easy showAnything` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
