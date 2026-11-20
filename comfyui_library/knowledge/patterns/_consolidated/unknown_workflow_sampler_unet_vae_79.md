---
name: unknown_workflow_sampler_unet_vae_79
type: Unknown Workflow
frequency: 13
level: moderate
coverage: 0.922923
common_nodes: [CLIPLoader, KSampler, LoadImage, QwenImage21Cache, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json, 图片生成/图生图/人物照片六种精修工具_2109075675494834178.json, 图片生成/图生图/六种风格_2108026478259691522.json, 图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json, 图片生成/图生图/诺亚数字人_Qwen 2.1换脸工作流_2114543156766265345.json, 图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2114885548811833346.json, 图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115628610513104897.json, 图片生成/图生图/诺亚数字人_Qwen_2.1换脸工作流_2115673430904360961.json, 图片生成/图生图/（10图）qwen-image-2.1多图编辑_2107971848804855810.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108408117536059393.json, 图片生成/文生图/AI生图编辑丨Qwen-Image 2.1丨多图参考·智能提示词老邵_2108416050982375426.json, 图片生成/文生图/Qwen Image2.1 图生图任意角度转换双图版_2105241162926878722.json, 平台全量/QwenImage2.1-换头&换脸_2119621158348869633.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_79

> 由 `engine/knowledge_consolidation` 从 13 个 workflow 归纳得出（图片生成/图生图/三图换姿换装｜Qwen2.1 姿势+人物+服装一次生成_2115719220301488129.json、图片生成/图生图/人物照片六种精修工具_2109075675494834178.json、图片生成/图生图/六种风格_2108026478259691522.json、图片生成/图生图/林茜数字人_Qwen 2.1换脸工作流_2112738971427106817.json、图片生成/图生图/诺亚数字人_Qwen 2.1换脸工作流_2114543156766265345.json…）

- **类型**：Unknown Workflow
- **样本数**：13
- **可信度**：中等可信
- **平均知识覆盖**：92%

## 共有节点

全部 13 个 workflow 都包含：
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
- `LoraLoaderModelOnly` —— 7/13 个有
- `Image Comparer (rgthree)` —— 6/13 个有
- `CR Text` —— 5/13 个有
- `ImageScaleToTotalPixels` —— 5/13 个有
- `JjkText` —— 2/13 个有
- `BatchImagesNode` —— 1/13 个有
- `PoseGallery` —— 1/13 个有
- `TextGenerateLTX2Prompt` —— 1/13 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 50 | 13 | 70% |
| Prompt 约束强度(CFG) | 1 | 1 - 3 | 13 | 42% |
| 采样算法 | euler | - | 13 | 100% |
| 调度器 | simple | - | 13 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 13 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 50，13 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 3，13 个样本，取值分散，一致性仅 42%
- 采样算法 最常用 euler，13 个样本，一致性 100%
- 调度器 最常用 simple，13 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，13 个样本，取值集中（一致性 100%）
