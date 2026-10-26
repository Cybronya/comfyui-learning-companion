---
name: unknown_workflow_video_lora_sampler_168
type: Unknown Workflow
frequency: 12
level: strong
coverage: 0.518333
common_nodes: [CLIPLoader, CLIPTextEncode, Fast Groups Bypasser (rgthree), GetImagesFromBatchIndexed, INTConstant, Int, JoinStrings, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, ModelSamplingSD3, PainterI2V, PathchSageAttentionKJ, PreviewImage, Qwen3_VQA, TextInput_, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy showAnything]
problems: []
missing: []
members: [视频生成/图生视频/XingRUI图生视频工作流（720P横屏）+V：jfr-1988获取软件_2020365816381841410.json, 视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流 720P图生视频+V：dxyc2291获取软件_2019556133358276609.json, 视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流-720P横屏_2028271741587431426.json, 视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流（720P横屏）_2038255613351829505.json, 视频生成/图生视频/万象AI-图生视频动态优化工作流（720P）_2019042589701316609.json, 视频生成/图生视频/二次元图生视频-动漫专用DaSiWa V9_2014552922826219521.json, 视频生成/图生视频/动漫单图生视频-动漫模型-DaSiWa v9-图生视频_2012098237326434305.json, 视频生成/图生视频/图生视频_2027704519647305729.json, 视频生成/图生视频/批量图生视频工作流720P32帧自动工作流_2021547239155437569.json, 视频生成/图生视频/涂经理图生视频工作流（720P横屏）+V：a2447548665获取软件_2019677447897227266.json, 视频生成/图生视频/爆款二创720P图生视频工作流  20260109_2002722598842691586.json, 视频生成/文生视频/万象+runninghub制作动漫短剧图生视频工作流（720P横屏）+V：50259731获取软件_2002624985527119873.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_168

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/图生视频/XingRUI图生视频工作流（720P横屏）+V：jfr-1988获取软件_2020365816381841410.json、视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流 720P图生视频+V：dxyc2291获取软件_2019556133358276609.json、视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流-720P横屏_2028271741587431426.json、视频生成/图生视频/万象+runninghub制作动漫短剧图生视频工作流（720P横屏）_2038255613351829505.json、视频生成/图生视频/万象AI-图生视频动态优化工作流（720P）_2019042589701316609.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：52%

## 共有节点

全部 12 个 workflow 都包含：
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
- `TextInput_`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `easy cleanGpuUsed` —— 11/12 个有
- `CR Integer To String` —— 10/12 个有
- `CR Text Replace` —— 10/12 个有
- `MathExpression|pysssss` —— 10/12 个有
- `RIFE VFI` —— 10/12 个有
- `ShowText|pysssss` —— 10/12 个有
- `Text Concatenate` —— 10/12 个有
- `Text Multiline` —— 10/12 个有
- `wanBlockSwap` —— 10/12 个有
- `GetAudioDurationFromAudio` —— 9/12 个有
- `LoadAudio` —— 9/12 个有
- `SimpleMath+` —— 2/12 个有
- `easy convertAnything` —— 2/12 个有
- `ImageOnlyCheckpointLoader` —— 1/12 个有
- `SONICSampler` —— 1/12 个有
- `SONICTLoader` —— 1/12 个有
- `SONIC_PreData` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 100% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 12 | 100% |
| 采样算法 | 1 | 1 - 1 | 12 | 100% |
| 调度器 | euler | - | 12 | 100% |
| 重绘幅度 | normal | - | 12 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，12 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，12 个样本，一致性 100%
- 重绘幅度 最常用 normal，12 个样本，一致性 83%
