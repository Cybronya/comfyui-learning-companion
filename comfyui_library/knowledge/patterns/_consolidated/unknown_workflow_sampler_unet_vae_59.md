---
name: unknown_workflow_sampler_unet_vae_59
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8967
common_nodes: [EmptyLatentImage, KSampler, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Z-image文生图_2016708585073414145.json, 图片生成/文生图/qwen_image2.文生图_2101942968000278530.json, 图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json, 图片生成/文生图/qwen_image_2_1_t2i_2101938471274369025.json, 图片生成/文生图/qwen_image_2_1_文生图_2101842315596886018.json, 图片生成/文生图/qwen_image_2_1文生图_2101884688183947265.json, 图片生成/文生图/【开源】Qwen image 2.1 文生图_2102002816368857089.json, 图片生成/文生图/【遇见AI】qwen image 2.1文生图基础流_2101841432792363010.json, 图片生成/文生图/千问2.1文生图_2101907864641167362.json, 数字人/数字人/qwen_image_2_1_角色三视图生成(自定义服装)_2108073982967762946.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_59

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/文生图/Z-image文生图_2016708585073414145.json、图片生成/文生图/qwen_image2.文生图_2101942968000278530.json、图片生成/文生图/qwen_image_2.1 _ 文生图_2103128462868443138.json、图片生成/文生图/qwen_image_2_1_t2i_2101938471274369025.json、图片生成/文生图/qwen_image_2_1_文生图_2101842315596886018.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 10 个 workflow 都包含：
- `EmptyLatentImage`
- `KSampler`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPLoader` —— 9/10 个有
- `ResolutionSelector` —— 9/10 个有
- `TextEncodeQwenImage21` —— 9/10 个有
- `JjkText` —— 3/10 个有
- `SaveImageAdvanced` —— 3/10 个有
- `LoadImage` —— 2/10 个有
- `Text` —— 2/10 个有
- `LoraLoaderModelOnly` —— 1/10 个有
- `RHHiddenNodes` —— 1/10 个有
- `easy promptList` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 1024 | 1024 - 1440 | 10 | 88% |
| 高度 | 1024 | 1024 - 1920 | 10 | 76% |
| 采样步数 | 25 | 10 - 40 | 10 | 73% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 1024，观测区间 1024 - 1440，10 个样本，取值集中（一致性 88%）
- 高度 中位数 1024，观测区间 1024 - 1920，10 个样本
- 采样步数 中位数 25，观测区间 10 - 40，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
