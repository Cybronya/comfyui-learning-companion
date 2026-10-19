---
name: unknown_workflow_video_lora_sampler_167
type: Unknown Workflow
frequency: 11
level: weak
coverage: 0.517727
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), GetImagesFromBatchIndexed, INTConstant, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, RIFE VFI, ShowText|pysssss, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/2020365816381841410.json, 视频生成/图生视频/2033525595593773057.json, 视频生成/图生视频/2019556133358276609.json, 视频生成/图生视频/2028271741587431426.json, 视频生成/图生视频/2038255613351829505.json, 视频生成/图生视频/2019042589701316609.json, 视频生成/图生视频/2027704519647305729.json, 视频生成/图生视频/2021547239155437569.json, 视频生成/图生视频/2019677447897227266.json, 视频生成/图生视频/2002722598842691586.json, 视频生成/文生视频/万象+runninghub制作动漫短剧图生视频工作流（720P横屏）+V：50259731获取软件_2002624985527119873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_167

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（视频生成/图生视频/2020365816381841410.json、视频生成/图生视频/2033525595593773057.json、视频生成/图生视频/2019556133358276609.json、视频生成/图生视频/2028271741587431426.json、视频生成/图生视频/2038255613351829505.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：52%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `Fast Groups Bypasser (rgthree)`
- `GetImagesFromBatchIndexed`
- `INTConstant`
- `Int`
- `JoinStrings`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `ModelSamplingSD3`
- `PainterI2V`
- `PathchSageAttentionKJ`
- `PreviewImage`
- `Qwen3_VQA`
- `RIFE VFI`
- `ShowText|pysssss`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `CR Integer To String` —— 10/11 个有
- `CR Text Replace` —— 10/11 个有
- `MathExpression|pysssss` —— 10/11 个有
- `Text Concatenate` —— 10/11 个有
- `Text Multiline` —— 10/11 个有
- `TextInput_` —— 10/11 个有
- `easy cleanGpuUsed` —— 10/11 个有
- `wanBlockSwap` —— 10/11 个有
- `GetAudioDurationFromAudio` —— 9/11 个有
- `LoadAudio` —— 9/11 个有
- `ImageOnlyCheckpointLoader` —— 1/11 个有
- `JjkText` —— 1/11 个有
- `SONICSampler` —— 1/11 个有
- `SONICTLoader` —— 1/11 个有
- `SONIC_PreData` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 20 | 11 | 16% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | normal | - | 11 | 91% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 20，11 个样本，取值分散，一致性仅 16%
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 normal，11 个样本，一致性 91%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
