---
name: unknown_workflow_sampler_clip_unet_233
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.9425
common_nodes: [BasicGuider, CLIPLoader, CLIPTextEncode, KSamplerSelect, RandomNoise, SamplerCustomAdvanced, SaveImage, UNETLoader, VAEDecode, VAELoader, llama_cpp_instruct_adv, llama_cpp_model_loader]
problems: []
missing: []
members: [图片生成/文生图/Z-image turbo 图片生成 🔥v2_2015076364591828994.json, 图片生成/文生图/角色图片-反推-rh-Qwen3VL-模板_2014161890011779073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_233

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（图片生成/文生图/Z-image turbo 图片生成 🔥v2_2015076364591828994.json、图片生成/文生图/角色图片-反推-rh-Qwen3VL-模板_2014161890011779073.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 2 个 workflow 都包含：
- `BasicGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerSelect`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `llama_cpp_instruct_adv`
- `llama_cpp_model_loader`

**可变部分**（部分 workflow 才有）：
- `BasicScheduler` —— 1/2 个有
- `EmptyLatentImage` —— 1/2 个有
- `EmptySD3LatentImage` —— 1/2 个有
- `FlowMatchEulerDiscreteScheduler (Custom)` —— 1/2 个有
- `KSamplerAdvanced` —— 1/2 个有
- `LoadImage` —— 1/2 个有
- `LoraLoaderModelOnly` —— 1/2 个有
- `easy showAnything` —— 1/2 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 1 | 100% |
| Prompt 约束强度(CFG) | 20 | - | 1 | 100% |
| 采样算法 | 1 | - | 1 | 100% |
| 调度器 | dpmpp_3m_sde | - | 1 | 100% |
| 重绘幅度 | ddim_uniform | - | 1 | 100% |
| 宽度 | 1280 | - | 1 | 100% |
| 高度 | 768 | - | 1 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
