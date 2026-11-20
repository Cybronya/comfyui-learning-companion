---
name: unknown_workflow_lora_sampler_unet_71
type: Unknown Workflow
frequency: 9
level: moderate
coverage: 0.926444
common_nodes: [CLIPLoader, ConditioningZeroOut, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/Qwen-Edit-2511 多图融合｜电商海报_2005156835357323266.json, 图片生成/图生图/Qwen-Edit-2511万物迁移 人物一致性｜好用舒适版_2005158095372382209.json, 图片生成/图生图/Qwen-Image-Edit 2509：服装提取平铺图，一键精剪，电商设计神器！_1990597155977125890.json, 图片生成/图生图/Qwen-edit 模特换装｜电商模特_2005159083936284674.json, 图片生成/图生图/Qwen-edit-2511-单图编辑（Custom Irzjason节点）_2007389656383496193.json, 图片生成/图生图/Qwen-edit-2511-服装迁移（Utils 2.2）_2007382960336543746.json, 图片生成/图生图/Qwen-edit-2511-服装迁移（alpha）_2010704951634300930.json, 图片生成/图生图/qwen-edit-2509万物迁移升级版_1993190145077739521.json, 图片生成/图生图/换装多合一Qwen-Edit-2509图像编辑-升级版_1987707318982914050.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_71

> 由 `engine/knowledge_consolidation` 从 9 个 workflow 归纳得出（图片生成/图生图/Qwen-Edit-2511 多图融合｜电商海报_2005156835357323266.json、图片生成/图生图/Qwen-Edit-2511万物迁移 人物一致性｜好用舒适版_2005158095372382209.json、图片生成/图生图/Qwen-Image-Edit 2509：服装提取平铺图，一键精剪，电商设计神器！_1990597155977125890.json、图片生成/图生图/Qwen-edit 模特换装｜电商模特_2005159083936284674.json、图片生成/图生图/Qwen-edit-2511-单图编辑（Custom Irzjason节点）_2007389656383496193.json…）

- **类型**：Unknown Workflow
- **样本数**：9
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 9 个 workflow 都包含：
- `CLIPLoader`
- `ConditioningZeroOut`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 6/9 个有
- `QwenEditConfigPreparer` —— 5/9 个有
- `TextEncodeQwenImageEditPlusCustom_lrzjason` —— 5/9 个有
- `Image Comparer (rgthree)` —— 4/9 个有
- `SDVN QwenEdit TextEncoder Plus` —— 4/9 个有
- `Text Multiline` —— 4/9 个有
- `ImageConcanate` —— 1/9 个有
- `Mask Fill Holes` —— 1/9 个有
- `PreviewImage` —— 1/9 个有
- `PrimitiveStringMultiline` —— 1/9 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 6 - 20 | 9 | 52% |
| Prompt 约束强度(CFG) | 2.5 | 1 - 2.5 | 9 | 59% |
| 采样算法 | euler | - | 9 | 100% |
| 调度器 | beta57 | - | 9 | 67% |
| 重绘幅度 | 1 | 1 - 1 | 9 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 4/9 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 20，观测区间 6 - 20，9 个样本
- Prompt 约束强度(CFG) 中位数 2.5，观测区间 1 - 2.5，9 个样本
- 采样算法 最常用 euler，9 个样本，一致性 100%
- 调度器 最常用 beta57，9 个样本，一致性 67%
- 重绘幅度 中位数 1，观测区间 1 - 1，9 个样本，取值集中（一致性 100%）
