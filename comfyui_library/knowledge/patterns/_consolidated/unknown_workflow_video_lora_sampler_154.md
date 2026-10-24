---
name: unknown_workflow_video_lora_sampler_154
type: Unknown Workflow
frequency: 11
level: strong
coverage: 0.292455
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, Fast Groups Bypasser (rgthree), GetNode, ImageBatchExtendWithOverlap, KSamplerAdvanced, LayerUtility: PurgeVRAM, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PrimitiveInt, SetNode, ShowText|pysssss, SomethingToString, Split String, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanAdvancedI2V, easy int]
problems: []
missing: []
members: [图片生成/图生图/SVI2Pro 全自动反推长视频_2009674822111989761.json, 视频生成/图生视频/(一致性)Wan2.2 Remix v2.1 + SVI2Pro +FLMF全自动提示词图生视频V1_2010956569466376194.json, 视频生成/图生视频/Wan2.2 Dasiwa V10+ SVI2 +Qwen3.5全自动提示词图生长视频V1_2040996955320487938.json, 视频生成/图生视频/Wan2.2 Remix v2.0 + SVI2Pro +FLMF全自动提示词图生视频V1_2010980319209459714.json, 视频生成/图生视频/Wan2.2 Remix v3 + SVI2 +Qwen3.5全自动提示词图生长视频V1_2035643021630377985.json, 视频生成/图生视频/Wan2.2 Remix v3 + SVI2 +Qwen3.5全自动提示词图生长视频V1_2036995772033540097.json, 视频生成/图生视频/Wan2.2 Smooth V2+ SVI2Pro +FLMF全自动提示词图生视频V1_2010983920858308609.json, 视频生成/图生视频/（N SFW）Wan2.2 Smooth V3+ SVI2Pro+Qwen3.5全自动提示词图生长视_2037035317777141762.json, 视频生成/图生视频/（自用）Wan2.2 Dasiwa V10+ SVI2Pro+Qwen3.5全自动提示词图生长视频_2040996971149795330.json, 视频生成/图生视频/（自用）Wan2.2 Smooth V2+ SVI2Pro +全自动提示词图生视频V1_2011039757379313666.json, 视频生成/图生视频/（自用）Wan2.2 Smooth V3+ SVI2Pro+Qwen3.5全自动提示词图生长视频V2_2035651804888829954.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_154

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（图片生成/图生图/SVI2Pro 全自动反推长视频_2009674822111989761.json、视频生成/图生视频/(一致性)Wan2.2 Remix v2.1 + SVI2Pro +FLMF全自动提示词图生视频V1_2010956569466376194.json、视频生成/图生视频/Wan2.2 Dasiwa V10+ SVI2 +Qwen3.5全自动提示词图生长视频V1_2040996955320487938.json、视频生成/图生视频/Wan2.2 Remix v2.0 + SVI2Pro +FLMF全自动提示词图生视频V1_2010980319209459714.json、视频生成/图生视频/Wan2.2 Remix v3 + SVI2 +Qwen3.5全自动提示词图生长视频V1_2035643021630377985.json…）

- **类型**：Unknown Workflow
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：29%

## 共有节点

全部 11 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `Fast Groups Bypasser (rgthree)`
- `GetNode`
- `ImageBatchExtendWithOverlap`
- `KSamplerAdvanced`
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
- `JWInteger` —— 10/11 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 10/11 个有
- `CR Text Concatenate` —— 8/11 个有
- `TextPreview` —— 8/11 个有
- `ShellAgentPluginOutputText` —— 6/11 个有
- `easy cleanGpuUsed` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `llama_cpp_instruct_adv` —— 6/11 个有
- `llama_cpp_model_loader` —— 6/11 个有
- `llama_cpp_parameters` —— 6/11 个有
- `DuckHideNode` —— 5/11 个有
- `Qwen3_VQA` —— 5/11 个有
- `SaveImage` —— 5/11 个有
- `TT_img_enc` —— 5/11 个有
- `TT_img_enc_v2` —— 5/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 11 | 100% |
| Prompt 约束强度(CFG) | 6 | 6 - 6 | 11 | 100% |
| 采样算法 | 1 | 1 - 1 | 11 | 100% |
| 调度器 | euler | - | 11 | 100% |
| 重绘幅度 | simple | - | 11 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，11 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 6，观测区间 6 - 6，11 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，11 个样本，一致性 100%
- 重绘幅度 最常用 simple，11 个样本，一致性 100%
