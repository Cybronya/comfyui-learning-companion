---
name: unknown_workflow_upscale_17
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 0.947571
common_nodes: [ImageUpscaleWithModel, LoadImage, SaveImage, UpscaleModelLoader]
problems: []
missing: []
members: [图片生成/图生图/普通放大--不透明1011_2109121126667476994.json, 图片生成/图生图/超分+加噪声增加真实度_1981305628402638849.json, 图片生成/图生图/高清放大_基础版_2068227997240479746.json, 平台全量/AI图片放大-超分模型通用增强_2103055480837992449.json, 平台全量/ComfyUi-放大图片工作流_1934947788910469121.json, 平台全量/图像高清放大-极简版_1884416735188078593.json, 数字人/数字人/超分+加噪声增加真实度_1982730089727180802.json]
source: knowledge_consolidation
---

# unknown_workflow_upscale_17

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（图片生成/图生图/普通放大--不透明1011_2109121126667476994.json、图片生成/图生图/超分+加噪声增加真实度_1981305628402638849.json、图片生成/图生图/高清放大_基础版_2068227997240479746.json、平台全量/AI图片放大-超分模型通用增强_2103055480837992449.json、平台全量/ComfyUi-放大图片工作流_1934947788910469121.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：95%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageUpscaleWithModel`
- `LoadImage`
- `SaveImage`
- `UpscaleModelLoader`

**可变部分**（部分 workflow 才有）：
- `LayerFilter: AddGrain` —— 2/7 个有
- `easy ifElse` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
