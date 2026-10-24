---
name: image_to_image_sampler_clip_vae_32
type: Image To Image
frequency: 5
level: weak
coverage: 0.9264
common_nodes: [CLIPLoader, CLIPTextEncode, KSampler, LoadImage, PreviewImage, SaveImage, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json, 图片生成/文生图/Anima图生图_2021929700087566337.json, 图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json, 图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json, 图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_vae_32

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（图片生成/文生图/Anima Aesthetic 1.1｜图生图_2078374866838974465.json、图片生成/文生图/Anima图生图_2021929700087566337.json、图片生成/文生图/草扎草编工艺_灯具设计_斗笠型_2098035544990244865.json、图片生成/文生图/草扎草编工艺_灯具设计_灯笼型_2098035451851530241.json、图片生成/文生图/草扎草编工艺_灯具设计_鱼篓型_2098023963254419458.json）

- **类型**：Image To Image
- **样本数**：5
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：93%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSampler`
- `LoadImage`
- `PreviewImage`
- `SaveImage`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `LoraLoaderModelOnly` —— 4/5 个有
- `UNETLoader` —— 4/5 个有
- `CannyEdgePreprocessor` —— 3/5 个有
- `ReferenceLatent` —— 3/5 个有
- `Qwen3VLProcessor` —— 2/5 个有
- `image_scale_pixel_v2` —— 2/5 个有
- `ClownsharKSampler_Beta` —— 1/5 个有
- `EnhancedLoadDiffusionModel` —— 1/5 个有
- `XB_UNetNameBroadcaster` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 22 | 20 - 31 | 4 | 81% |
| Prompt 约束强度(CFG) | 4 | 4 - 31 | 5 | 0% |
| 采样算法 | euler | - | 5 | 60% |
| 调度器 | simple | - | 5 | 80% |
| 重绘幅度 | 0.95 | 0.7 - 4 | 5 | 17% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 22，观测区间 20 - 31，4 个样本，取值集中（一致性 81%）
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 31，5 个样本，取值分散，一致性仅 0%
- 采样算法 最常用 euler，5 个样本，一致性 60%
- 调度器 最常用 simple，5 个样本，一致性 80%
- 重绘幅度 中位数 0.95，观测区间 0.7 - 4，5 个样本，取值分散，一致性仅 17%
- 风险：Prompt 约束强度(CFG) 观测到 31，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
- 风险：重绘幅度 观测到 4，超出安全上限 1（denoise 接近 1.0 时接近重新生成，初始潜空间影响被抹平）
