---
name: unknown_workflow_generic_50
type: Unknown Workflow
frequency: 20
level: moderate
coverage: 0.8259
common_nodes: [LoadImage, SaveImage, SeeThrough_GenerateDepth, SeeThrough_GenerateLayers, SeeThrough_LoadDepthModel, SeeThrough_LoadLayerDiffModel, SeeThrough_PostProcess, SeeThrough_SavePSD]
problems: []
missing: []
members: [图片生成/图生图/See Through-图像超级分层_2040236988468563969.json, 图片生成/图生图/SeeThrough--卡通--PSD完整分层_2039999402210762754.json, 图片生成/图生图/SeeThrough--真人--PSD完整分层_2040001077692600322.json, 图片生成/图生图/SeeThrough_二次元PSD分层、拆图-live2D_动画_游戏_2040012380536578050.json, 图片生成/图生图/SeeThrough_二次元PSD分层、拆图-live2D_动画_游戏_2052228852306464770.json, 图片生成/图生图/SeeThrough二次元卡通PSD完整分层工作流V1_2039958431506898945.json, 图片生成/图生图/SeeThrough二次元卡通PSD完整分层工作流V1_2040046165248450562.json, 图片生成/图生图/SeeThrough分层工作流_2049314933434753026.json, 图片生成/图生图/SeeThrough图像PSD完整分层工作流V1_2044008357320728578.json, 图片生成/图生图/SeeThrough图像分层_2040064434797813762.json, 图片生成/图生图/SeeThrough图像拆分_2077199511004471297.json, 图片生成/图生图/SeeThrough真人PSD完整分层工作流V1_2039976374139625473.json, 图片生成/图生图/二次元拆分分层输出PSD-SeeThrough_2040420040951996417.json, 图片生成/图生图/图像分层  PSD  SeeThrough_2040216332402171906.json, 图片生成/图生图/图像分层 -—— PSD_2051294797817757697.json, 图片生成/图生图/图像分层 -—— PSD_2068728786014789633.json, 图片生成/图生图/图像分层 PSD SeeThrough  抠图_2069610389201047553.json, 图片生成/图生图/图像分层_PSD_SeeThrough_抠图_2052600759396651009.json, 图片生成/图生图/图像分层_PSD_SeeThrough_抠图_2057499012751781889.json, 图片生成/图生图/图层拆分 SeeThrough_2040211441290055681.json]
source: knowledge_consolidation
---

# unknown_workflow_generic_50

> 由 `engine/knowledge_consolidation` 从 20 个 workflow 归纳得出（图片生成/图生图/See Through-图像超级分层_2040236988468563969.json、图片生成/图生图/SeeThrough--卡通--PSD完整分层_2039999402210762754.json、图片生成/图生图/SeeThrough--真人--PSD完整分层_2040001077692600322.json、图片生成/图生图/SeeThrough_二次元PSD分层、拆图-live2D_动画_游戏_2040012380536578050.json、图片生成/图生图/SeeThrough_二次元PSD分层、拆图-live2D_动画_游戏_2052228852306464770.json…）

- **类型**：Unknown Workflow
- **样本数**：20
- **可信度**：中等可信
- **平均知识覆盖**：83%

## 共有节点

全部 20 个 workflow 都包含：
- `LoadImage`
- `SaveImage`
- `SeeThrough_GenerateDepth`
- `SeeThrough_GenerateLayers`
- `SeeThrough_LoadDepthModel`
- `SeeThrough_LoadLayerDiffModel`
- `SeeThrough_PostProcess`
- `SeeThrough_SavePSD`

**可变部分**（部分 workflow 才有）：
- `PreviewImage` —— 16/20 个有
- `easy cleanGpuUsed` —— 7/20 个有
- `Fast Groups Bypasser (rgthree)` —— 3/20 个有
- `Image Comparer (rgthree)` —— 3/20 个有
- `InspyrenetRembg` —— 3/20 个有
- `MaskToImage` —— 3/20 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 2/20 个有
- `LayerUtility: PurgeVRAM` —— 1/20 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
