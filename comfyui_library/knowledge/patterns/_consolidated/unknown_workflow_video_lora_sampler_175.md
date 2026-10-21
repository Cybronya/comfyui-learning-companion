---
name: unknown_workflow_video_lora_sampler_175
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.2938
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, ImageBatchExtendWithOverlap, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SetNode, ShowText|pysssss, SomethingToString, Split String, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanAdvancedI2V, easy int]
problems: []
missing: []
members: [视频生成/图生视频/2010956569466376194.json, 视频生成/图生视频/2040996955320487938.json, 视频生成/图生视频/2010980319209459714.json, 视频生成/图生视频/2035643021630377985.json, 视频生成/图生视频/2036995772033540097.json, 视频生成/图生视频/2010983920858308609.json, 视频生成/图生视频/2037035317777141762.json, 视频生成/图生视频/2040996971149795330.json, 视频生成/图生视频/2011039757379313666.json, 视频生成/图生视频/2035651804888829954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_175

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（视频生成/图生视频/2010956569466376194.json、视频生成/图生视频/2040996955320487938.json、视频生成/图生视频/2010980319209459714.json、视频生成/图生视频/2035643021630377985.json、视频生成/图生视频/2036995772033540097.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：29%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PrimitiveInt`
- `SetNode`
- `ShowText|pysssss`
- `SomethingToString`
- `Split String`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanAdvancedI2V`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `CR Text Concatenate` —— 7/10 个有
- `TextPreview` —— 7/10 个有
- `ShellAgentPluginOutputText` —— 6/10 个有
- `easy cleanGpuUsed` —— 6/10 个有
- `easy showAnything` —— 6/10 个有
- `llama_cpp_instruct_adv` —— 6/10 个有
- `llama_cpp_model_loader` —— 6/10 个有
- `llama_cpp_parameters` —— 6/10 个有
- `DuckHideNode` —— 5/10 个有
- `SaveImage` —— 5/10 个有
- `TT_img_enc` —— 5/10 个有
- `TT_img_enc_v2` —— 5/10 个有
- `Qwen3_VQA` —— 4/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 10 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 10 | 100% |
| 采样算法 | 1 | 1 - 1 | 10 | 100% |
| 调度器 | euler | - | 10 | 100% |
| 重绘幅度 | simple | - | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，10 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，10 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，10 个样本，一致性 100%
- 重绘幅度 最常用 simple，10 个样本，一致性 100%
