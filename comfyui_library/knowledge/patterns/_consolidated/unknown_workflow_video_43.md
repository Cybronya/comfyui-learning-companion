---
name: unknown_workflow_video_43
type: Unknown Workflow
frequency: 7
level: moderate
coverage: 1
common_nodes: [ImageScaleToTotalPixels, LoadImage, ReActorFaceBoost, ReActorFaceSwap, VHS_LoadVideo, VHS_VideoCombine, VHS_VideoInfo]
problems: []
missing: []
members: [平台全量/旅拍机-旅拍视频-备选正脸参数版-慢速暂停_2071283097307533314.json, 平台全量/视频换脸 极速高清放大版_2033735019813933058.json, 平台全量/视频换脸+极速高清放大版_2056336150335410177.json, 平台全量/视频换脸_输入参数_视频上传_正脸图片_最终版_2052931431793475585.json, 平台全量/（最终版）视频换脸 极速高清放大版_2052754107588460546.json, 视频生成/图生视频/三脸+视频换脸+自定义时长+精度_2077007977915174913.json, 视频生成/图生视频/视频换脸_1920378379508584450.json]
source: knowledge_consolidation
---

# unknown_workflow_video_43

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/旅拍机-旅拍视频-备选正脸参数版-慢速暂停_2071283097307533314.json、平台全量/视频换脸 极速高清放大版_2033735019813933058.json、平台全量/视频换脸+极速高清放大版_2056336150335410177.json、平台全量/视频换脸_输入参数_视频上传_正脸图片_最终版_2052931431793475585.json、平台全量/（最终版）视频换脸 极速高清放大版_2052754107588460546.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：中等可信
- **平均知识覆盖**：100%

## 共有节点

全部 7 个 workflow 都包含：
- `ImageScaleToTotalPixels`
- `LoadImage`
- `ReActorFaceBoost`
- `ReActorFaceSwap`
- `VHS_LoadVideo`
- `VHS_VideoCombine`
- `VHS_VideoInfo`

**可变部分**（部分 workflow 才有）：
- `WujiCleaner` —— 6/7 个有
- `ReActorBuildFaceModel` —— 5/7 个有
- `ImageConcanate` —— 4/7 个有
- `Int` —— 1/7 个有
- `MathExpression|pysssss` —— 1/7 个有
- `Wav2Lip` —— 1/7 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
