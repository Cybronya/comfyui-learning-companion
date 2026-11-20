---
name: image_to_image_controlnet_upscale_sampler
type: Image To Image
frequency: 12
level: moderate
coverage: 0.7785
common_nodes: [AIO_Preprocessor, BRIA_RMBG_ModelLoader_Zho, BRIA_RMBG_Zho, BrushNet, BrushNetLoader, CLIPSetLastLayer, CLIPTextEncode, CheckpointLoaderSimple, ControlNetApplyAdvanced, ControlNetLoader, GrowMask, ImageResize+, ImageUpscaleWithModel, ImpactDilateMask, InvertMask, KSampler, LoadImage, PreviewImage, RepeatLatentBatch, SaveImage, UpscaleModelLoader, VAEDecode, VAEEncode, VAELoader, preview_mask]
problems: []
missing: []
members: [平台全量/可乐_罐装饮料 拍摄广告_1812677792222863361.json, 平台全量/咖啡机商品图摄影_1807671436113850369.json, 平台全量/室内设计手稿-原木风家居转换器_1797811268577521666.json, 平台全量/服装摄影大片换背景_1813455340590526465.json, 平台全量/白瓷壶商品图摄影_1808830603507773442.json, 平台全量/箱包商品图摄影_1810871928560742402.json, 平台全量/背包商品图摄影_1796372501710880770.json, 平台全量/背包商品图摄影_1824356445121851394.json, 平台全量/茶壶商品图摄影_1797453465895579649.json, 平台全量/载具车背景替换_1811320588016742401.json, 平台全量/运动鞋产品拍摄图_1810234154149146626.json, 平台全量/香水商品图摄影_1797501651666341889.json]
source: knowledge_consolidation
---

# image_to_image_controlnet_upscale_sampler

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（平台全量/可乐_罐装饮料 拍摄广告_1812677792222863361.json、平台全量/咖啡机商品图摄影_1807671436113850369.json、平台全量/室内设计手稿-原木风家居转换器_1797811268577521666.json、平台全量/服装摄影大片换背景_1813455340590526465.json、平台全量/白瓷壶商品图摄影_1808830603507773442.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：78%

## 共有节点

全部 12 个 workflow 都包含：
- `AIO_Preprocessor`
- `BRIA_RMBG_ModelLoader_Zho`
- `BRIA_RMBG_Zho`
- `BrushNet`
- `BrushNetLoader`
- `CLIPSetLastLayer`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `ControlNetApplyAdvanced`
- `ControlNetLoader`
- `GrowMask`
- `ImageResize+`
- `ImageUpscaleWithModel`
- `ImpactDilateMask`
- `InvertMask`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `RepeatLatentBatch`
- `SaveImage`
- `UpscaleModelLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`
- `preview_mask`

**可变部分**（部分 workflow 才有）：
- `GetNode` —— 10/12 个有
- `Image Overlay` —— 10/12 个有
- `ImageScale` —— 10/12 个有
- `SetNode` —— 10/12 个有
- `IPAdapter` —— 8/12 个有
- `IPAdapterUnifiedLoader` —— 8/12 个有
- `LayerColor: ColorAdapter` —— 8/12 个有
- `Mask Gaussian Region` —— 6/12 个有
- `LayerColor: RGB` —— 4/12 个有
- `ImageToMask` —— 2/12 个有
- `MaskToImage` —— 2/12 个有
- `AegisFlow/aflogo` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| ControlNet 权重 | 0.675 | 0.6 - 1 | 12 | 76% |
| 采样步数 | 20 | 20 - 27 | 12 | 91% |
| Prompt 约束强度(CFG) | 7 | 7 - 7 | 12 | 100% |
| 采样算法 | dpmpp_2m_sde_gpu | - | 12 | 50% |
| 调度器 | karras | - | 12 | 75% |
| 重绘幅度 | 0.48 | 0.15 - 1 | 12 | 40% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- ControlNet 权重 中位数 0.675，观测区间 0.6 - 1，12 个样本
- 采样步数 中位数 20，观测区间 20 - 27，12 个样本，取值集中（一致性 91%）
- Prompt 约束强度(CFG) 中位数 7，观测区间 7 - 7，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m_sde_gpu，12 个样本，一致性 50%
- 调度器 最常用 karras，12 个样本，一致性 75%
- 重绘幅度 中位数 0.48，观测区间 0.15 - 1，12 个样本，取值分散，一致性仅 40%
