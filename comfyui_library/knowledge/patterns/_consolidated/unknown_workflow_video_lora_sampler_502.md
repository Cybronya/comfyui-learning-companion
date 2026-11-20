---
name: unknown_workflow_video_lora_sampler_502
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9152
common_nodes: [CreateCFGScheduleFloatList, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoVAELoader]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json, 视频生成/图生视频/wan2.2图生视频_自动润色提示词_1950857744138043393.json, 视频生成/图生视频/动漫已保留去水印版，自用_(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1973249582245220353.json, 视频生成/图生视频/反推Lightx2v高动态图生视频_1982131363547619329.json, 视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_502

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（视频生成/图生视频/Wan2.2高动态宫崎骏动漫图生视频_1991013397888180225.json、视频生成/图生视频/wan2.2图生视频_自动润色提示词_1950857744138043393.json、视频生成/图生视频/动漫已保留去水印版，自用_(insight+ani全能视频Sv3新版)wan2.2高动态卡通动漫图生视频加速版v1_1973249582245220353.json、视频生成/图生视频/反推Lightx2v高动态图生视频_1982131363547619329.json、视频生成/图生视频/图生视频（Wan2.2-V1）高质量加速版_1950432359721123842.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 5 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoVAELoader`

**可变部分**（部分 workflow 才有）：
- `Float` —— 4/5 个有
- `GetImageSizeAndCount` —— 4/5 个有
- `INTConstant` —— 4/5 个有
- `JWInteger` —— 4/5 个有
- `WanVideoScheduler` —— 4/5 个有
- `WanVideoSigmaToStep` —— 4/5 个有
- `WanVideoSetBlockSwap` —— 3/5 个有
- `WanVideoSetLoRAs` —— 3/5 个有
- `WanVideoTorchCompileSettings` —— 3/5 个有
- `CR Prompt Text` —— 2/5 个有
- `LayerUtility: PurgeVRAM` —— 2/5 个有
- `RH_Captioner` —— 2/5 个有
- `RH_LLMAPI_NODE` —— 2/5 个有
- `AILab_QwenVL` —— 1/5 个有
- `CR Text` —— 1/5 个有
- `CR Text Concatenate` —— 1/5 个有
- `ImageFromBatch+` —— 1/5 个有
- `ImpactSwitch` —— 1/5 个有
- `LayerUtility: TextJoinV2` —— 1/5 个有
- `ShowText|pysssss` —— 1/5 个有
- `easy int` —— 1/5 个有
- `easy seed` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
