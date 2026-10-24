---
name: unknown_workflow_lora_sampler_unet_109
type: Unknown Workflow
frequency: 6
level: moderate
coverage: 0.943333
common_nodes: [BatchImagesNode, CLIPLoader, EmptyLatentImage, KSampler, LoadImage, LoraLoaderModelOnly, QwenImage21Cache, ResolutionSelector, SaveImage, TextEncodeQwenImage21, TextGenerateLTX2Prompt, UNETLoader, VAEDecode, VAELoader, easy showAnything]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json, 图片生成/图生图/文生图_参考生图2合1_2108194083813552130.json, 图片生成/图生图/文生图_参考生图2合1改_2110563178919845889.json, 图片生成/图生图/文生图_参考生图2合1改_2111007047281111042.json, 图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json, 图片生成/文生图/文生图_参考生图2合1（改）_2108160229987938306.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_109

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/Qwen image 2.1单图编辑4K版_2101843086979719170.json、图片生成/图生图/文生图_参考生图2合1_2108194083813552130.json、图片生成/图生图/文生图_参考生图2合1改_2110563178919845889.json、图片生成/图生图/文生图_参考生图2合1改_2111007047281111042.json、图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：中等可信
- **平均知识覆盖**：94%

## 共有节点

全部 6 个 workflow 都包含：
- `BatchImagesNode`
- `CLIPLoader`
- `EmptyLatentImage`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `QwenImage21Cache`
- `ResolutionSelector`
- `SaveImage`
- `TextEncodeQwenImage21`
- `TextGenerateLTX2Prompt`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `easy showAnything`

**可变部分**（部分 workflow 才有）：
- `SaveImageAdvanced` —— 5/6 个有
- `llama_cpp_instruct_adv` —— 5/6 个有
- `llama_cpp_model_loader` —— 5/6 个有
- `JjkText` —— 2/6 个有
- `ComfySwitchNode` —— 1/6 个有
- `KOOK_ImageCompression` —— 1/6 个有
- `KOOK_SaveJPGImage` —— 1/6 个有
- `PreviewImage` —— 1/6 个有
- `SeedVR2LoadDiTModel` —— 1/6 个有
- `SeedVR2LoadVAEModel` —— 1/6 个有
- `SeedVR2VideoUpscaler` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 1 - 20 | 6 | 58% |
| Prompt 约束强度(CFG) | 8 | 1 - 8 | 6 | 62% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 0.3 - 1 | 6 | 70% |
| 宽度 | 1024 | 512 - 1024 | 6 | 80% |
| 高度 | 1024 | 512 - 1024 | 6 | 80% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 1/6 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 1 - 20，6 个样本
- Prompt 约束强度(CFG) 中位数 8，观测区间 1 - 8，6 个样本
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 0.3 - 1，6 个样本
- 宽度 中位数 1024，观测区间 512 - 1024，6 个样本
- 高度 中位数 1024，观测区间 512 - 1024，6 个样本
