---
name: unknown_workflow_video_lora_sampler_657
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.871333
common_nodes: [CreateCFGScheduleFloatList, DF_Integer, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_LLMAPI_NODE, RH_Translator, ShowText|pysssss, SimpleMath+, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy int, string_util_StrReplace]
problems: []
missing: []
members: [视频生成/图生视频/wan2.2视频生成+视频反推配音_1964312846312067074.json, 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json, 视频生成/图生视频/图生视频_1965606390897233921.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_657

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（视频生成/图生视频/wan2.2视频生成+视频反推配音_1964312846312067074.json、视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json、视频生成/图生视频/图生视频_1965606390897233921.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 3 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_LLMAPI_NODE`
- `RH_Translator`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Multiline`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoImageToVideoEncode`
- `WanVideoLoraSelect`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoSetBlockSwap`
- `WanVideoSetLoRAs`
- `WanVideoTextEncode`
- `WanVideoVAELoader`
- `easy int`
- `string_util_StrReplace`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 2/3 个有
- `WanVideoTorchCompileSettings` —— 2/3 个有
- `easy ifElse` —— 2/3 个有
- `AILab_MiniCPM_4_V_Advanced` —— 1/3 个有
- `GetVideoComponents` —— 1/3 个有
- `HunyuanVideoFoley` —— 1/3 个有
- `ImpactSwitch` —— 1/3 个有
- `LoadAudio` —— 1/3 个有
- `LoadVideo` —— 1/3 个有
- `PreviewAudio` —— 1/3 个有
- `RH_Captioner` —— 1/3 个有
- `Text Concatenate` —— 1/3 个有
- `easy clearCacheAll` —— 1/3 个有
- `easy showAnything` —— 1/3 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
