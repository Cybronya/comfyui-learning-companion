---
name: unknown_workflow_video_lora_vae_4
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.958
common_nodes: [LoadImage, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoEmptyEmbeds, WanVideoExperimentalArgs, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSLG, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTeaCache, WanVideoTextEncodeCached, WanVideoTorchCompileSettings, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/2067523198845014018.json, 视频生成/图生视频/2062115572657254402.json, 视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 文生视频_2070787856590786562.json, 视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_vae_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（视频生成/图生视频/2067523198845014018.json、视频生成/图生视频/2062115572657254402.json、视频生成/文生视频/【遇见AI】wan2.1 MoviiGen影视美学 文生视频_2070787856590786562.json、视频生成/文生视频/【遇见AI】wan2.1 Skyreels V2 文生视频，支持超过81帧_2067520501110632450.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：96%

## 共有节点

全部 4 个 workflow 都包含：
- `LoadImage`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoEmptyEmbeds`
- `WanVideoExperimentalArgs`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSLG`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTeaCache`
- `WanVideoTextEncodeCached`
- `WanVideoTorchCompileSettings`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `WanVideoEnhanceAVideo` —— 3/4 个有
- `WanVideoSampler` —— 3/4 个有
- `GetImageRangeFromBatch` —— 1/4 个有
- `GetImageSizeAndCount` —— 1/4 个有
- `ImageBatchMulti` —— 1/4 个有
- `SimpleMath+` —— 1/4 个有
- `WanVideoDiffusionForcingSampler` —— 1/4 个有
- `WanVideoEncode` —— 1/4 个有
- `WanVideoVRAMManagement` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
