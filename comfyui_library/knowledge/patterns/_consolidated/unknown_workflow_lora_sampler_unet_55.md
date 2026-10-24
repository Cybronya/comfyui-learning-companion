---
name: unknown_workflow_lora_sampler_unet_55
type: Unknown Workflow
frequency: 10
level: strong
coverage: 0.8451
common_nodes: [CLIPLoader, KSampler, LoadImage, LoraLoaderModelOnly, SaveImage, TextEncodeQwenImageEditPlusAdvance_lrzjason, UNETLoader, VAEDecode, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json, 图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json, 图片生成/图生图/换装商用级 高度一致性 高清_2104130241412292610.json, 图片生成/图生图/换装简洁版 换衣简洁版   电商服装展示 FireRed-Image-Edit 小红书_2079795242282340354.json, 图片生成/图生图/电商换装丨双图服装试穿_2100138204581163009.json, 图片生成/图生图/电商换装丨双图服装试穿_2101857775021281282.json, 图片生成/图生图/电商换装丨双图服装试穿_2102673132061552641.json, 图片生成/图生图/电商服装展示_换装 换衣_2078741577014534146.json, 图片生成/文生图/Qwen_手写字体生成_2054073147015614466.json, 图片生成/文生图/Qwen美食解构海报+全节点注释_2055916690986291201.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_unet_55

> 由 `engine/knowledge_consolidation` 从 10 个 workflow 归纳得出（图片生成/图生图/图生图丨美食解构海报_2054801927573123073.json、图片生成/图生图/换装+换衣+电商+FireRed-Image-Edit+多件服饰批量叠穿_2092526645906329601.json、图片生成/图生图/换装商用级 高度一致性 高清_2104130241412292610.json、图片生成/图生图/换装简洁版 换衣简洁版   电商服装展示 FireRed-Image-Edit 小红书_2079795242282340354.json、图片生成/图生图/电商换装丨双图服装试穿_2100138204581163009.json…）

- **类型**：Unknown Workflow
- **样本数**：10
- **可信度**：强结论
- **平均知识覆盖**：85%

## 共有节点

全部 10 个 workflow 都包含：
- `CLIPLoader`
- `KSampler`
- `LoadImage`
- `LoraLoaderModelOnly`
- `SaveImage`
- `TextEncodeQwenImageEditPlusAdvance_lrzjason`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `ConditioningZeroOut` —— 9/10 个有
- `PreviewImage` —— 7/10 个有
- `PIP_图像联结` —— 6/10 个有
- `seed _O` —— 3/10 个有
- `Image Comparer (rgthree)` —— 2/10 个有
- `Text _O` —— 2/10 个有
- `TextCombinerTwo` —— 2/10 个有
- `easy showAnything` —— 2/10 个有
- `JjkText` —— 1/10 个有
- `MultiTextConcatenate` —— 1/10 个有
- `PreviewAny` —— 1/10 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 8 | 10 | 65% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 10 | 100% |
| 采样算法 | euler | - | 10 | 100% |
| 调度器 | simple | - | 10 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 10 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 15/10 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 8，10 个样本
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 采样算法 最常用 euler，10 个样本，一致性 100%
- 调度器 最常用 simple，10 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，10 个样本，取值集中（一致性 100%）
- 高发问题（15/10 个样本）：Steps较低可能导致细节不足
