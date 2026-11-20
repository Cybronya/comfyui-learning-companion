---
name: unknown_workflow_video_lora_sampler_125
type: Unknown Workflow
frequency: 14
level: moderate
coverage: 0.866143
common_nodes: [CreateCFGScheduleFloatList, DF_Integer, INTConstant, JWInteger, LoadWanVideoT5TextEncoder, MathExpression|pysssss, RH_Translator, SimpleMath+, Text Multiline, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoLoraSelect, WanVideoModelLoader, WanVideoSampler, WanVideoSetBlockSwap, WanVideoSetLoRAs, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVAELoader, easy int]
problems: []
missing: []
members: [图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json, 视频生成/图生视频/Wan2.2+文生视频+-+KJ加速版+-+提示词自动优化_2055178416466472962.json, 视频生成/图生视频/wan2.2 kj版_1955015931215822850.json, 视频生成/图生视频/wan2.2 人物动态海报视频 - KJ加速优化版_1955449911829565441.json, 视频生成/图生视频/wan2.2 图生视频 - KJ加速优化版_1950571192820420609.json, 视频生成/图生视频/wan2.2 图生视频 - KJ加速优化版_1955912718601650177.json, 视频生成/图生视频/wan2.2 图生视频 - 加速优化版_1957829417538088962.json, 视频生成/图生视频/wan2.2 图生视频_1953992101455548418.json, 视频生成/图生视频/wan2.2 批量图生自动生成视频 +补帧60fps_1973675102011305986.json, 视频生成/图生视频/静态漫画视频生成ez_1995801916682670082.json, 视频生成/文生视频/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_1950600207669088257.json, 视频生成/文生视频/Wan2.2文生视频+KJ加速版+提示词自动优化_2055539394576166914.json, 视频生成/文生视频/Wan2.2文生视频+KJ加速版+提示词自动优化_2056240799226093570.json, 视频生成/文生视频/wan2.2 图生视频 -  超级加速晋级版_1967469611824373761.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_125

> 由 `engine/knowledge_consolidation` 从 14 个 workflow 归纳得出（图片生成/文生图/Wan2.2 文生视频 - KJ加速版 - 提示词自动优化_2044313653356273666.json、视频生成/图生视频/Wan2.2+文生视频+-+KJ加速版+-+提示词自动优化_2055178416466472962.json、视频生成/图生视频/wan2.2 kj版_1955015931215822850.json、视频生成/图生视频/wan2.2 人物动态海报视频 - KJ加速优化版_1955449911829565441.json、视频生成/图生视频/wan2.2 图生视频 - KJ加速优化版_1950571192820420609.json…）

- **类型**：Unknown Workflow
- **样本数**：14
- **可信度**：中等可信
- **平均知识覆盖**：87%

## 共有节点

全部 14 个 workflow 都包含：
- `CreateCFGScheduleFloatList`
- `DF_Integer`
- `INTConstant`
- `JWInteger`
- `LoadWanVideoT5TextEncoder`
- `MathExpression|pysssss`
- `RH_Translator`
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
- `GetImageSizeAndCount` —— 13/14 个有
- `PrimitiveBoolean` —— 13/14 个有
- `ShowText|pysssss` —— 13/14 个有
- `easy ifElse` —— 13/14 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 8/14 个有
- `LoadImage` —— 8/14 个有
- `WanVideoImageToVideoEncode` —— 8/14 个有
- `RH_Captioner` —— 7/14 个有
- `RH_LLMAPI_NODE` —— 7/14 个有
- `string_util_StrReplace` —— 7/14 个有
- `CR Text` —— 6/14 个有
- `CR Text Concatenate` —— 6/14 个有
- `RH_Prompter` —— 6/14 个有
- `WanVideoEmptyEmbeds` —— 6/14 个有
- `DownloadAndLoadGIMMVFIModel` —— 2/14 个有
- `GIMMVFI_interpolate` —— 2/14 个有
- `Display Int (rgthree)` —— 1/14 个有
- `PreviewImage` —— 1/14 个有
- `easy batchAnything` —— 1/14 个有
- `easy cleanGpuUsed` —— 1/14 个有
- `easy forLoopEnd` —— 1/14 个有
- `easy forLoopStart` —— 1/14 个有
- `easy imageIndexSwitch` —— 1/14 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
