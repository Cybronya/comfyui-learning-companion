---
name: unknown_workflow_video_lora_sampler_862
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.8455
common_nodes: [CreateCFGScheduleFloatList, DF_Integer, GetImageSizeAndCount, INTConstant, JWInteger, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoadWanVideoT5TextEncoder, MathExpression|pysssss, PrimitiveBoolean, RH_LLMAPI_NODE, RH_Translator, ShowText|pysssss, SimpleMath+, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoImageToVideoEncode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoVAELoader, easy ifElse, easy int, string_util_StrReplace]
problems: []
missing: []
members: [视频生成/图生视频/1964312846312067074.json, 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_862

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/1964312846312067074.json、视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：85%

## 共有节点

全部 2 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `PrimitiveBoolean`
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
- `easy ifElse`
- `easy int`
- `string_util_StrReplace`

**可变部分**（部分 workflow 才有）：
- `AILab_MiniCPM_4_V_Advanced` —— 1/2 个有
- `GetVideoComponents` —— 1/2 个有
- `HunyuanVideoFoley` —— 1/2 个有
- `ImpactSwitch` —— 1/2 个有
- `LoadVideo` —— 1/2 个有
- `PreviewAudio` —— 1/2 个有
- `RH_Captioner` —— 1/2 个有
- `Text Concatenate` —— 1/2 个有
- `WanVideoTorchCompileSettings` —— 1/2 个有
- `easy clearCacheAll` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
