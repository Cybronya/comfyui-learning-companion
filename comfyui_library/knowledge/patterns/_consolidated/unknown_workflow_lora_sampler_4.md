---
name: unknown_workflow_lora_sampler_4
type: Unknown Workflow
frequency: 4
level: moderate
coverage: 0.7605
common_nodes: [CR Prompt Text, CalligrapherBlockSwap, CalligrapherImageProcesssor, CalligrapherLora, CalligrapherModelLoader, CalligrapherSampler, GrowMaskWithBlur, LayerUtility: ImageScaleByAspectRatio V2, LayerUtility: PurgeVRAM, LoadImage, MaskToImage, PreviewImage, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Calligrapher单步骤极速文字编辑（交叉引用版）_1944066975452762113.json, 图片生成/图生图/Calligrapher单步骤极速文字编辑（自引用版）_1944064211175505922.json, 图片生成/图生图/Calligrapher单步骤极速文字编辑（非文本引用版）_1943996948556709889.json, 图片生成/图生图/Calligrapher自由文字方便面版_1944042463516327938.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_4

> 由 `engine/knowledge_consolidation` 从 4 个 workflow 归纳得出（图片生成/图生图/Calligrapher单步骤极速文字编辑（交叉引用版）_1944066975452762113.json、图片生成/图生图/Calligrapher单步骤极速文字编辑（自引用版）_1944064211175505922.json、图片生成/图生图/Calligrapher单步骤极速文字编辑（非文本引用版）_1943996948556709889.json、图片生成/图生图/Calligrapher自由文字方便面版_1944042463516327938.json）

- **类型**：Unknown Workflow
- **样本数**：4
- **可信度**：中等可信
- **平均知识覆盖**：76%

## 共有节点

全部 4 个 workflow 都包含：
- `CR Prompt Text`
- `CalligrapherBlockSwap`
- `CalligrapherImageProcesssor`
- `CalligrapherLora`
- `CalligrapherModelLoader`
- `CalligrapherSampler`
- `GrowMaskWithBlur`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LayerUtility: PurgeVRAM`
- `LoadImage`
- `MaskToImage`
- `PreviewImage`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `ImageConcanate` —— 3/4 个有
- `ImageResizeKJ` —— 3/4 个有
- `PMRF` —— 3/4 个有
- `LayerUtility: PurgeVRAM V2` —— 1/4 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
