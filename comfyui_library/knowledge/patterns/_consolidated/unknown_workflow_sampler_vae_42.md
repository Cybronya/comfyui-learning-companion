---
name: unknown_workflow_sampler_vae_42
type: Unknown Workflow
frequency: 5
level: moderate
coverage: 0.9858
common_nodes: [LoadImage, MegaStyleModelLoader, MegaStyleSampler, MegaStyleTextEncode, MegaStyleVAEDecode, MegaStyleVAEEncode, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Megastyle-风格迁移_2057805875473117185.json, 图片生成/图生图/megastyle风格迁移V1_2057290894960840706.json, 图片生成/图生图/megastyle风格迁移V1_2058061286075879425.json, 图片生成/图生图/megastyle风格迁移（适合做数据集）_2056613476650541057.json, 图片生成/图生图/图像风格迁移参考megastyle_2057752730151768066.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_vae_42

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/图生图/Megastyle-风格迁移_2057805875473117185.json、图片生成/图生图/megastyle风格迁移V1_2057290894960840706.json、图片生成/图生图/megastyle风格迁移V1_2058061286075879425.json、图片生成/图生图/megastyle风格迁移（适合做数据集）_2056613476650541057.json、图片生成/图生图/图像风格迁移参考megastyle_2057752730151768066.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 5 个 workflow 都包含：
- `LoadImage`
- `MegaStyleModelLoader`
- `MegaStyleSampler`
- `MegaStyleTextEncode`
- `MegaStyleVAEDecode`
- `MegaStyleVAEEncode`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 4/5 个有
- `ImageConcanate` —— 3/5 个有
- `AddLabel` —— 2/5 个有
- `DeepTranslatorTextNode` —— 1/5 个有
- `GetImageSize` —— 1/5 个有
- `Int` —— 1/5 个有
- `easy showAnything` —— 1/5 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
