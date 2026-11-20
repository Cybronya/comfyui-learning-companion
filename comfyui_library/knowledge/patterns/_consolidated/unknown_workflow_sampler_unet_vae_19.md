---
name: unknown_workflow_sampler_unet_vae_19
type: Unknown Workflow
frequency: 19
level: weak
coverage: 0.941632
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json, 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json, 图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json, 图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json, 图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json, 图片生成/图生图/图片编辑_qwenimage 2.1_2101829437766586370.json, 图片生成/图生图/多图编辑qwen image2.1_2102573736280023041.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2104737905183903746.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105235774793928705.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2105274061088706562.json, 图片生成/图生图/换头换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2111625667644317697.json, 图片生成/图生图/换脸Face+Swap++Qwen-Image-2.1模特换头+换脸_2102936104516280321.json, 图片生成/图生图/文生图_参考生图2合1_2108194083813552130.json, 图片生成/图生图/文生图_参考生图2合1改_2110563178919845889.json, 图片生成/图生图/文生图_参考生图2合1改_2111007047281111042.json, 图片生成/文生图/image2.1文生图_参考生图2合1_2109107304275730434.json, 图片生成/文生图/qwen image2.1多图编辑_2101927769339940865.json, 图片生成/文生图/qwen+image+2.1多图编辑_2102637659226206209.json, 图片生成/文生图/文生图_参考生图2合1（改）_2108160229987938306.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_19

> 由 `engine/knowledge_consolidation` 从 19 个 workflow 归纳得出（图片生成/图生图/qwen image2.1多图编辑工作流_2112804506063949825.json、图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102232455502716929.json、图片生成/图生图/qwen-image-2.1一键抠图 PNG通道_2102236996667265025.json、图片生成/图生图/qwen-image-2.1图生图_2101823764827828226.json、图片生成/图生图/qwen-image-2.1图生图（三套夏装)_2107744199545278466.json…）

- **类型**：Unknown Workflow
- **样本数**：19
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：94%

## 共有节点

全部 19 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `QwenImage21Cache`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `BatchImagesNode` —— 15/19 个有
- `EmptyLatentImage` —— 15/19 个有
- `TextGenerateLTX2Prompt` —— 15/19 个有
- `ResolutionSelector` —— 12/19 个有
- `SaveImageAdvanced` —— 11/19 个有
- `easy showAnything` —— 10/19 个有
- `ComfySwitchNode` —— 7/19 个有
- `JjkText` —— 7/19 个有
- `CR Text` —— 6/19 个有
- `LoraLoaderModelOnly` —— 5/19 个有
- `llama_cpp_instruct_adv` —— 5/19 个有
- `llama_cpp_model_loader` —— 5/19 个有
- `JDCN_StringToList` —— 3/19 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 50 | 19 | 59% |
| Prompt 约束强度(CFG) | 1 | 1 - 8 | 19 | 1% |
| 采样算法 | euler | - | 19 | 100% |
| 调度器 | simple | - | 19 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 19 | 100% |
| 宽度 | 1024 | 1024 - 1920 | 15 | 78% |
| 高度 | 1024 | 1024 - 2560 | 15 | 58% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 50，19 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 8，19 个样本，取值分散，一致性仅 1%
- 采样算法 最常用 euler，19 个样本，一致性 100%
- 调度器 最常用 simple，19 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，19 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1920，15 个样本
- 高度 中位数 1024，观测区间 1024 - 2560，15 个样本
