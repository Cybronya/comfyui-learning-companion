---
name: unknown_workflow_generic_173
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.988083
common_nodes: [LoadImage, RH_ComfyFluxKontext, SaveImage]
problems: []
missing: []
members: [图片生成/图生图/Flux Kontext 生成企业形象照_1928578146331926529.json, 图片生成/图生图/Flux Kontext 老照片修复_1928594881076404226.json, 图片生成/图生图/明城墙明朝还原_1934872692094869506.json, 图片生成/图生图/明城墙明朝还原_1935178440431554561.json, 图片生成/文生图/Kontext-max一句话修改文字增加人物_1931560252347756545.json, 图片生成/文生图/Kontext-max一句话生成熊猫宝宝_1931553605239943170.json, 图片生成/文生图/Kontext-max一句话给橘子宝宝加耳朵_1931555932394684418.json, 图片生成/文生图/一句话换装发色加耳环_1931563283378319361.json, 平台全量/FLUX.1 Kontext多图融合保持一致性_1934927429259436034.json, 平台全量/PS高阶-一键证件照_1955169800869875714.json, 平台全量/一句话换发型发色唇色衣服背景加纹身_1938114629740728321.json, 视频生成/图生视频/kontext_flux技术测评_1928633296190652418.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_173

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/Flux Kontext 生成企业形象照_1928578146331926529.json、图片生成/图生图/Flux Kontext 老照片修复_1928594881076404226.json、图片生成/图生图/明城墙明朝还原_1934872692094869506.json、图片生成/图生图/明城墙明朝还原_1935178440431554561.json、图片生成/文生图/Kontext-max一句话修改文字增加人物_1931560252347756545.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `LoadImage`
- `RH_ComfyFluxKontext`
- `SaveImage`

**可变部分**（部分 workflow 才有）：
- `LayerUtility: ImageScaleByAspectRatio V2` —— 11/12 个有
- `ImageConcanate` —— 10/12 个有
- `DeepTranslatorTextNode` —— 6/12 个有
- `RHHiddenNodes` —— 5/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
