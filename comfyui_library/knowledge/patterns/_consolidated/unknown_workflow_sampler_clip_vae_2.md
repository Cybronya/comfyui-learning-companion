---
name: unknown_workflow_sampler_clip_vae_2
type: Unknown Workflow
frequency: 22
level: weak
coverage: 0.962182
common_nodes: [CLIPLoader, CLIPTextEncode, EmptySD3LatentImage, KSampler, SaveImage, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json, 图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json, 图片生成/文生图/Qwen-Image-Lightning_1954757119348240386.json, 图片生成/文生图/Qwen-Image-一键中文海报直出_1953001917527093249.json, 图片生成/文生图/Qwen-Image-生成角色三视图_1966728561858162689.json, 图片生成/文生图/Qwen-Image_1967210141957361665.json, 图片生成/文生图/Qwen-Image_1971395682378661889.json, 图片生成/文生图/Qwen-Image一键生成不知火舞真实版_2042047842927255553.json, 图片生成/文生图/Qwen-Image文生图古风女生_1953303428673040385.json, 图片生成/文生图/Qwen-Image文生图水墨人物_1953747187043848193.json, 图片生成/文生图/Qwen-Image文生图能吃苦_1953318467875295234.json, 图片生成/文生图/Qwen-Image文生图花和尚_1953307722135572481.json, 图片生成/文生图/Qwen-Image文生图（lora基础使用工作流）_1954190525895196674.json, 图片生成/文生图/Qwen-Image的8步加速_1954463793558515714.json, 图片生成/文生图/Qwen-image 8步极速生图_1954559302579187713.json, 图片生成/文生图/Qwen-image-2512 文生图_2009132641324376066.json, 图片生成/文生图/Qwen-image中式插画_1965257014656028674.json, 图片生成/文生图/Qwen2512腿精巨长腿背影杀腿部调节_2019638224775290882.json, 图片生成/文生图/QwenImage千问文生图4步加速放大工作流_1955919657263923201.json, 图片生成/文生图/z-image滑块系列文生图_2057114517376688130.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2024871763326275585.json, 图片生成/文生图/性感情趣内衣亮亮丝袜_2110944951742844929.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_vae_2

> 由 `engine/knowledge_consolidation` 从 22 个 workflow 归纳得出（图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1955586331033288705.json、图片生成/文生图/Qwen-Image-GGUF-Q4KS-4步极速生图_1970690059521454082.json、图片生成/文生图/Qwen-Image-Lightning_1954757119348240386.json、图片生成/文生图/Qwen-Image-一键中文海报直出_1953001917527093249.json、图片生成/文生图/Qwen-Image-生成角色三视图_1966728561858162689.json…）

- **类型**：Unknown Workflow
- **样本数**：22
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：96%

## 共有节点

全部 22 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptySD3LatentImage`
- `KSampler`
- `SaveImage`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ModelSamplingAuraFlow` —— 21/22 个有
- `LoraLoaderModelOnly` —— 20/22 个有
- `UNETLoader` —— 20/22 个有
- `CompressImages` —— 4/22 个有
- `easy seed` —— 3/22 个有
- `UnetLoaderGGUF` —— 2/22 个有
- `CR Upscale Image` —— 1/22 个有
- `PrimitiveFloat` —— 1/22 个有
- `String Literal` —— 1/22 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 30 | 22 | 37% |
| Prompt 约束强度(CFG) | 1 | 1 - 4 | 22 | 32% |
| 采样算法 | euler | - | 22 | 91% |
| 调度器 | simple | - | 22 | 91% |
| 重绘幅度 | 1 | 1 - 1 | 22 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 21/22 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 30，22 个样本，取值分散，一致性仅 37%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 4，22 个样本，取值分散，一致性仅 32%
- 采样算法 最常用 euler，22 个样本，一致性 91%
- 调度器 最常用 simple，22 个样本，一致性 91%
- 重绘幅度 中位数 1，观测区间 1 - 1，22 个样本，取值集中（一致性 100%）
- 高发问题（21/22 个样本）：Steps较低可能导致细节不足
