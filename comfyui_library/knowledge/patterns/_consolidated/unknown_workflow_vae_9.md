---
name: unknown_workflow_vae_9
type: Unknown Workflow
frequency: 3
level: strong
coverage: 0.737667
common_nodes: [EmptyLatentImage, Image Comparer (rgthree), LoadImage, PreviewImage, SaveImage, VAEEncode, VAELoader, workflow>双截棍加速kontext]
problems: []
missing: []
members: [平台全量/【阡陌】Nunchaku 加速Kontext超强一致性编辑_1948656782263615490.json, 平台全量/【阡陌】Nunchaku 加速Kontext遮罩转颜色指哪改哪万物移除_1949013800541401090.json, 平台全量/【阡陌】Nunchak加速Kontext开源版双图多图融合_1949011098780016642.json]
source: knowledge_consolidation
---

# unknown_workflow_vae_9

> 由 `engine/knowledge_consolidation` 从 3 个 workflow 归纳得出（平台全量/【阡陌】Nunchaku 加速Kontext超强一致性编辑_1948656782263615490.json、平台全量/【阡陌】Nunchaku 加速Kontext遮罩转颜色指哪改哪万物移除_1949013800541401090.json、平台全量/【阡陌】Nunchak加速Kontext开源版双图多图融合_1949011098780016642.json）

- **类型**：Unknown Workflow
- **样本数**：3
- **可信度**：强结论
- **平均知识覆盖**：74%

## 共有节点

全部 3 个 workflow 都包含：
- `EmptyLatentImage`
- `Image Comparer (rgthree)`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEEncode`
- `VAELoader`
- `workflow>双截棍加速kontext`

**可变部分**（部分 workflow 才有）：
- `FluxKontextImageScale` —— 2/3 个有
- `ImageConcanate` —— 1/3 个有
- `LayerUtility: ColorPicker` —— 1/3 个有
- `workflow>遮罩转颜色` —— 1/3 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 512 | 512 - 600 | 3 | 92% |
| 高度 | 512 | 512 - 800 | 3 | 78% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 宽度 中位数 512，观测区间 512 - 600，3 个样本，取值集中（一致性 92%）
- 高度 中位数 512，观测区间 512 - 800，3 个样本
