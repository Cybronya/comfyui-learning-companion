---
name: unknown_workflow_lora_sampler_clip_196
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.833
common_nodes: [Any Switch (rgthree), CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, Int, KSamplerAdvanced, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, SaveImage, SimpleMath+, UNETLoader, UnetLoaderGGUF, VAEDecode, VAELoader, easy negative, easy positive, easy showAnything]
problems: []
missing: []
members: [图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json, 图片生成/文生图/QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json, 图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_196

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/文生图/QT103-文生图双引擎（Wan2.2）自动提示词润色，一句话也也能出完美图像，wan2.2文生图_1956342842593607682.json、图片生成/文生图/QY5-情境穿搭四幕剧（Wan2.2）千姿百态，电商、模特、服装，人物一致性+高清放大，万物迁移_1949359850576347138.json、图片生成/文生图/Wan2.2文生图 扣子api调用_1963968525272498177.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 3 个 workflow 都包含：
- `Any Switch (rgthree)`
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `Int`
- `KSamplerAdvanced`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SaveImage`
- `SimpleMath+`
- `UNETLoader`
- `UnetLoaderGGUF`
- `VAEDecode`
- `VAELoader`
- `easy negative`
- `easy positive`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `Fast Groups Bypasser (rgthree)` —— 2/3 个有
- `PlaySound|pysssss` —— 2/3 个有
- `Wan_video_prompt_generator` —— 2/3 个有
- `easy bookmark` —— 2/3 个有
- `easy int` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `RHHiddenNodes` —— 1/3 个有
- `RH_LLMAPI_NODE` —— 1/3 个有
- `RunningHub SeedXPro Translator` —— 1/3 个有
- `UpscaleModelLoader` —— 1/3 个有
- `easy cleanGpuUsed` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 3 | 67% |
| Prompt 约束强度(CFG) | 12 | 12 - 12 | 3 | 100% |
| 采样算法 | 2.5 | 1 - 2.5 | 3 | 65% |
| 调度器 | euler | - | 3 | 100% |
| 重绘幅度 | simple | - | 3 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，3 个样本，一致性 67%
- Prompt 约束强度(CFG) 中位数 12，观测区间 12 - 12，3 个样本，取值集中（一致性 100%）
- 采样算法 中位数 2.5，观测区间 1 - 2.5，3 个样本
- 调度器 最常用 euler，3 个样本，一致性 100%
- 重绘幅度 最常用 simple，3 个样本，一致性 100%
