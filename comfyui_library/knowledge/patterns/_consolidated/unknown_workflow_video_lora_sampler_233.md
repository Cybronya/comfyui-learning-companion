---
name: unknown_workflow_video_lora_sampler_233
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.86
common_nodes: [CreateCFGScheduleFloatList, DF_Integer, GetImageSizeAndCount, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Translator, ShowText|pysssss, SimpleMath+, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: [CR Text, CR Text Concatenate, MathExpression|pysssss, SimpleMath+, Text Multiline, easy int]
members: [视频生成/图生视频/2055178416466472962.json, 视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json, 视频生成/图生视频/1965606390897233921.json, 视频生成/图生视频/1995801916682670082.json, 视频生成/文生视频/1950600207669088257.json, 视频生成/文生视频/Wan2.2文生视频+KJ加速版+提示词自动优化_2055539394576166914.json, 视频生成/文生视频/Wan2.2文生视频+KJ加速版+提示词自动优化_2056240799226093570.json, 视频生成/文生视频/1967469611824373761.json, 视频生成/文生视频/wan2.2文生视频，加速版（自动润色提示词）_2006301824508239873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_233

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（视频生成/图生视频/2055178416466472962.json、视频生成/图生视频/【图生视频】WAN2.2-I2V-KJ加速优化版_1972179704662913025.json、视频生成/图生视频/1965606390897233921.json、视频生成/图生视频/1995801916682670082.json、视频生成/文生视频/1950600207669088257.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：86%

## 共有节点

全部 9 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `GetImageSizeAndCount`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Translator`
- `ShowText|pysssss`
- `SimpleMath+`
- `Text Multiline`
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
- `easy int`

**可变部分**（部分 workflow 才有）：
- `PrimitiveBoolean` —— 8/9 个有
- `easy ifElse` —— 8/9 个有
- `CR Text` —— 6/9 个有
- `CR Text Concatenate` —— 6/9 个有
- `RH_Prompter` —— 6/9 个有
- `WanVideoEmptyEmbeds` —— 6/9 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 3/9 个有
- `LoadImage` —— 3/9 个有
- `RH_LLMAPI_NODE` —— 3/9 个有
- `WanVideoImageToVideoEncode` —— 3/9 个有
- `string_util_StrReplace` —— 3/9 个有
- `DownloadAndLoadGIMMVFIModel` —— 1/9 个有
- `GIMMVFI_interpolate` —— 1/9 个有
- `LoadAudio` —— 1/9 个有
- `RH_Captioner` —— 1/9 个有
- `RIFE VFI` —— 1/9 个有
- `easy cleanGpuUsed` —— 1/9 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 这些节点还没有知识卡，系统对它们的理解有限：CR Text、CR Text Concatenate、MathExpression|pysssss、SimpleMath+、Text Multiline
