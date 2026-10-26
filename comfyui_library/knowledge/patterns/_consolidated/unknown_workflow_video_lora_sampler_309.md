---
name: unknown_workflow_video_lora_sampler_309
type: Unknown Workflow
frequency: 8
level: strong
coverage: 0.92275
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, CR Text, EmptyHunyuanLatentVideo, ImageFromBatch+, JWInteger, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, ShellAgentPluginOutputText, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, easy anythingIndexSwitch, easy cleanGpuUsed, easy showAnything, llama_cpp_instruct_adv, llama_cpp_model_loader, llama_cpp_parameters]
problems: []
missing: []
members: [视频生成/图生视频/Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json, 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035358127658377218.json, 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json, 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2036029728359976962.json, 视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json, 视频生成/文生视频/（N sfw版）Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035617850320228353.json, 视频生成/文生视频/（自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035392938565443585.json, 视频生成/文生视频/（贞贞lora-自用）N版Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035397258946027521.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_309

> 由 `engine/knowledge_consolidation` 从 8 个 workflow 归纳得出（视频生成/图生视频/Wan2.2 Smooth V3--Qwen3.5自动提示词--文生视频_2035656316517093377.json、视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频V1_2035358127658377218.json、视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2035617864299843586.json、视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频_2036029728359976962.json、视频生成/文生视频/Wan2.2 Smooth V3+Qwen3.5自动提示词文生视频工作流_2035941912657534978.json…）

- **类型**：Unknown Workflow
- **样本数**：8
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 8 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `CR Text`
- `EmptyHunyuanLatentVideo`
- `ImageFromBatch+`
- `JWInteger`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `ShellAgentPluginOutputText`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `easy anythingIndexSwitch`
- `easy cleanGpuUsed`
- `easy showAnything`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`
- `llama_cpp_parameters`

**可变部分**（部分 workflow 才有）：
- `Seed (rgthree)` —— 7/8 个有
- `DuckHideNode` —— 3/8 个有
- `LoadImage` —— 3/8 个有
- `SaveImage` —— 3/8 个有
- `TT_img_enc` —— 3/8 个有
- `TT_img_enc_v2` —— 3/8 个有
- `ConcatTextOfUtils` —— 1/8 个有
- `Int` —— 1/8 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 8 | 100% |
| Prompt 约束强度(CFG) | 8 | 8 - 8 | 8 | 100% |
| 采样算法 | 1 | 1 - 1 | 8 | 100% |
| 调度器 | euler | - | 8 | 100% |
| 重绘幅度 | simple | - | 8 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，8 个样本，一致性 100%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 8，8 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，8 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，8 个样本，一致性 100%
- 重绘幅度 最常用 simple，8 个样本，一致性 100%
