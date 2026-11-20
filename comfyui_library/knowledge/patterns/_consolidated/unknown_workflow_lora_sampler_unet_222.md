---
name: unknown_workflow_lora_sampler_unet_222
type: Unknown Workflow
frequency: 3
level: moderate
coverage: 0.772
common_nodes: [CLIPLoader, Image Comparer (rgthree), KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/qwen 自定义相机角度_2009814368095047681.json, 图片生成/图生图/qwen-edit-2509-动漫转真人_1988122840039845889.json, 视频生成/图生视频/【Qwen-Edit-2509】一键换装迁移_1985628103055683586.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_222

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（图片生成/图生图/qwen 自定义相机角度_2009814368095047681.json、图片生成/图生图/qwen-edit-2509-动漫转真人_1988122840039845889.json、视频生成/图生视频/【Qwen-Edit-2509】一键换装迁移_1985628103055683586.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：中等可信
- **平均知识覆盖**：77%

## 共有节点

全部 3 个 workflow 都包含：
- `CLIPLoader`
- `Image Comparer (rgthree)`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 2/3 个有
- `ImageConcanate` —— 2/3 个有
- `PreviewImage` —— 2/3 个有
- `CR Text` —— 1/3 个有
- `ImageResize+` —— 1/3 个有
- `QwenMultiangleCameraNode` —— 1/3 个有
- `TextEncodeQwenImageEditPlus` —— 1/3 个有
- `孤海图像缩放按像素` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 8 | 4 - 20 | 3 | 36% |
| Prompt 约束强度(CFG) | 1 | 1 - 2.5 | 3 | 53% |
| 采样算法 | lcm | - | 3 | 33% |
| 调度器 | beta57 | - | 3 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 3 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/3 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 8，观测区间 4 - 20，3 个样本，取值分散，一致性仅 36%
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 2.5，3 个样本
- 采样算法 最常用 lcm，3 个样本，一致性 33%
- 调度器 最常用 beta57，3 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，3 个样本，取值集中（一致性 100%）
- 高发问题（2/3 个样本）：Steps较低可能导致细节不足
