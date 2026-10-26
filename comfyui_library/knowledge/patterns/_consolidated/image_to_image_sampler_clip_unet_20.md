---
name: image_to_image_sampler_clip_unet_20
type: Image To Image
frequency: 12
level: strong
coverage: 0.993583
common_nodes: [CLIPTextEncode, DualCLIPLoader, KSampler, LoadImage, SaveImage, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/FLUX图生图工作流_2075049931479543809.json, 图片生成/图生图/Flux Krea图生图_1951057726677917698.json, 图片生成/图生图/Flux-dev-fp8-图生图_2064238323991932929.json, 图片生成/图生图/Flux图生图工作流_1912803304072540161.json, 图片生成/图生图/Flux图生图工作流_1980482281401925633.json, 图片生成/图生图/Flux图生图工作流_1985262437538668545.json, 图片生成/图生图/Flux图生图工作流_1992168901211648002.json, 图片生成/图生图/Flux图生图工作流_2007730863437516801.json, 图片生成/图生图/Flux图生图工作流_2008831243256864770.json, 图片生成/图生图/Flux图生图工作流产品设计_1918558384063451138.json, 图片生成/图生图/Flux图生图工作流（RunningHub拖入一键运行)_2090772341793054722.json, 图片生成/图生图/图生图工作流_2106376021615403010.json]
source: knowledge_consolidation
---

# image_to_image_sampler_clip_unet_20

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/FLUX图生图工作流_2075049931479543809.json、图片生成/图生图/Flux Krea图生图_1951057726677917698.json、图片生成/图生图/Flux-dev-fp8-图生图_2064238323991932929.json、图片生成/图生图/Flux图生图工作流_1912803304072540161.json、图片生成/图生图/Flux图生图工作流_1980482281401925633.json…）

- **类型**：Image To Image
- **样本数**：12
- **可信度**：强结论
- **平均知识覆盖**：99%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPTextEncode`
- `DualCLIPLoader`
- `KSampler`
- `LoadImage`
- `SaveImage`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPTextEncodeFlux` —— 11/12 个有
- `JWImageResizeByLongerSide` —— 11/12 个有
- `DF_Text_Box` —— 10/12 个有
- `ConditioningZeroOut` —— 1/12 个有
- `Image Comparer (rgthree)` —— 1/12 个有
- `ImageScaleDownToSize` —— 1/12 个有
- `easy imageConcat` —— 1/12 个有
- `easy positive` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 25 | 20 - 30 | 12 | 92% |
| Prompt 约束强度(CFG) | 1 | 1 - 1 | 12 | 100% |
| 采样算法 | dpmpp_2m | - | 12 | 92% |
| 调度器 | sgm_uniform | - | 12 | 92% |
| 重绘幅度 | 0.7 | 0.6 - 0.7 | 12 | 96% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 中位数 25，观测区间 20 - 30，12 个样本，取值集中（一致性 92%）
- Prompt 约束强度(CFG) 中位数 1，观测区间 1 - 1，12 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，12 个样本，一致性 92%
- 调度器 最常用 sgm_uniform，12 个样本，一致性 92%
- 重绘幅度 中位数 0.7，观测区间 0.6 - 0.7，12 个样本，取值集中（一致性 96%）
