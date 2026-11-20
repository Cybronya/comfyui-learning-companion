---
name: unknown_workflow_sampler_unet_vae_26
type: Unknown Workflow
frequency: 17
level: strong
coverage: 0.815
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json, 图片生成/图生图/千问_2104563424893161474.json, 图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json, 图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json, 图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json, 图片生成/图生图/千问工作流_2102311506384867330.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  qwen2.1图生图，图像编辑_2112866530273882114.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  图像编辑模式_2102150751400316930.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102152565902368769.json, 图片生成/图生图/开源最强图片模型 Qwen-image2.1  指定抠图模式_2102179241923272706.json, 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105107851831234562.json, 图片生成/图生图/开源最强图片模型_Qwen-image2.1_指定抠图模式_2105488254140239873.json, 图片生成/图生图/自动抠图 Qwen-image2.1_2103125967697956866.json, 图片生成/文生图/Qwen Image 2.1图像编辑_2101902551456243713.json, 图片生成/文生图/qwen image 2.1文生图生_2101747084268498945.json, 图片生成/文生图/千问 qwen image 2.1 单图编辑+全节点注释_2101953275674320897.json, 图片生成/文生图/千问 qwen image 2.1 多图编辑 图片编辑 +全节点注释_2101953245253033985.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_26

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（图片生成/图生图/千问2.1图像编辑工作流｜多图参考精准修改_2104511260204290049.json、图片生成/图生图/千问_2104563424893161474.json、图片生成/图生图/千问image2.1三图编辑_2101912050518814722.json、图片生成/图生图/千问image2.1单图编辑_2101910795029409794.json、图片生成/图生图/千问image2.1双图编辑_2101908220829851649.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：强结论
- **平均知识覆盖**：82%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ComfySwitchNode` —— 16/17 个有
- `EmptyLatentImage` —— 16/17 个有
- `QwenImage21Cache` —— 16/17 个有
- `CR Text` —— 14/17 个有
- `ResolutionSelector` —— 10/17 个有
- `孤海注释` —— 7/17 个有
- `TextGenerateLTX2Prompt` —— 4/17 个有
- `Note Plus (mtb)` —— 3/17 个有
- `Anything Everywhere3` —— 2/17 个有
- `CR Prompt Text` —— 2/17 个有
- `BatchImagesNode` —— 1/17 个有
- `EmptyImage` —— 1/17 个有
- `MultiTextConcatenate` —— 1/17 个有
- `PreviewImage` —— 1/17 个有
- `easy cleanGpuUsed` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 40 | 17 | 78% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 17 | 68% |
| 采样算法 | euler | - | 17 | 94% |
| 调度器 | simple | - | 17 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 1024 | 1024 - 1024 | 16 | 100% |
| 高度 | 1024 | 1024 - 1624 | 16 | 86% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 40，17 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，17 个样本
- 采样算法 最常用 euler，17 个样本，一致性 94%
- 调度器 最常用 simple，17 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 1024，观测区间 1024 - 1024，16 个样本，取值集中（一致性 100%）
- 高度 中位数 1024，观测区间 1024 - 1624，16 个样本，取值集中（一致性 86%）
