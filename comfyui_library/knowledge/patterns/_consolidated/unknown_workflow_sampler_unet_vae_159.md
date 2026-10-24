---
name: unknown_workflow_sampler_unet_vae_159
type: Unknown Workflow
frequency: 6
level: strong
coverage: 0.898333
common_nodes: [CLIPLoader, KSampler, LoadImage, SaveImage, TextEncodeQwenImage21, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json, 图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json, 图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json, 图片生成/图生图/QWEN_PANO360 全景图生成工作流_2109286054019817473.json, 图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json, 图片生成/图生图/Qwen Image 2.1 精准完美抠图｜自动修复遮挡区域_2104051381421305858.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_159

> 由 `engine/knowledge_consolidation` 从 6 个 workflow 归纳得出（图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2104392510440304641.json、图片生成/图生图/CHIEFAI-千问IMAGE2.1换头工作流_2111994819705925633.json、图片生成/图生图/CHIEFAI-千问IMAGE2.1立面迁移工作流_2102217964954152961.json、图片生成/图生图/QWEN_PANO360 全景图生成工作流_2109286054019817473.json、图片生成/图生图/Qwen Image 2.1 最强开源图像编辑【多图编辑】｜超强一致性｜模特换装_2101812329016025089.json…）

- **类型**：Unknown Workflow
- **样本数**：6
- **可信度**：强结论
- **平均知识覆盖**：90%

## 共有节点

全部 6 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `TextEncodeQwenImage21`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/6 个有
- `PrimitiveStringMultiline` —— 4/6 个有
- `EmptyLatentImage` —— 3/6 个有
- `ComfySwitchNode` —— 2/6 个有
- `Get resolution [Crystools]` —— 2/6 个有
- `QwenImage21Cache` —— 2/6 个有
- `AIO_Preprocessor` —— 1/6 个有
- `Text Find and Replace` —— 1/6 个有
- `Text Multiline` —— 1/6 个有
- `XinbaoImageStandardizer` —— 1/6 个有
- `孤海注释` —— 1/6 个有
- `忽略多组孤海` —— 1/6 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 25 - 25 | 6 | 100% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 6 | 100% |
| 采样算法 | euler | - | 6 | 100% |
| 调度器 | simple | - | 6 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 6 | 100% |
| 宽度 | 1536 | 1200 - 1600 | 3 | 88% |
| 高度 | 1200 | 768 - 2000 | 3 | 61% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 25 - 25，6 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，6 个样本，一致性 100%
- 调度器 最常用 simple，6 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，6 个样本，取值集中（一致性 100%）
- 宽度 中位数 1536，观测区间 1200 - 1600，3 个样本，取值集中（一致性 88%）
- 高度 中位数 1200，观测区间 768 - 2000，3 个样本
