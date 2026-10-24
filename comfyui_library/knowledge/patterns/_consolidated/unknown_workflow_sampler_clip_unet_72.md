---
name: unknown_workflow_sampler_clip_unet_72
type: Unknown Workflow
frequency: 12
level: moderate
coverage: 0.9255
common_nodes: [CFGGuider, CLIPLoader, CLIPTextEncode, ConditioningZeroOut, EmptyFlux2LatentImage, Flux2Scheduler, GetImageSize, KSamplerSelect, LoadImage, RandomNoise, ReferenceLatent, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAEEncode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/flux2 klein 任意位置皮肤完美克隆（无限制）_2012907749159473153.json, 图片生成/图生图/flux2-Klein-图像多角度生成_2012189967140786177.json, 图片生成/图生图/flux2-Klein-换脸(色差偏移修正版)_2012337568234344450.json, 图片生成/图生图/flux2-Klein-最快换脸_2012192553822593025.json, 图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json, 图片生成/图生图/kleinface 换头换脸工作流 Flux2-Klein-9B 人物换头AI智能面部替换高清换头脸_2016848786680713218.json, 图片生成/图生图/优化场景去除图像AI感 增加细节_2041708135127191554.json, 图片生成/图生图/去除图像AI感 增加细节_2032271913573158914.json, 图片生成/图生图/去除图像AI感 增加细节_2036273754577313794.json, 图片生成/图生图/场景去除图像AI感 增加细节_2032342155766796289.json, 图片生成/图生图/场景去除图像AI感+增加细节_2046436726729613313.json, 图片生成/文生图/去除图像AI感 去油腻质感，增加细节纹理，防止僵尸脸_2093538755654275073.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_72

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（图片生成/图生图/flux2 klein 任意位置皮肤完美克隆（无限制）_2012907749159473153.json、图片生成/图生图/flux2-Klein-图像多角度生成_2012189967140786177.json、图片生成/图生图/flux2-Klein-换脸(色差偏移修正版)_2012337568234344450.json、图片生成/图生图/flux2-Klein-最快换脸_2012192553822593025.json、图片生成/图生图/flux2.klein一键高清换装_2077230946503446529.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：中等可信
- **平均知识覆盖**：93%

## 共有节点

全部 12 个 workflow 都包含：
- `CFGGuider`
- `CLIPLoader`
- `CLIPTextEncode`
- `ConditioningZeroOut`
- `EmptyFlux2LatentImage`
- `Flux2Scheduler`
- `GetImageSize`
- `KSamplerSelect`
- `LoadImage`
- `RandomNoise`
- `ReferenceLatent`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAEEncode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `SaveImage` —— 11/12 个有
- `Image Comparer (rgthree)` —— 9/12 个有
- `ImageScaleToTotalPixels` —— 8/12 个有
- `ImageResize+` —— 7/12 个有
- `ColorMatch` —— 6/12 个有
- `DetailDaemonSamplerNode` —— 6/12 个有
- `ImageSharpen` —— 6/12 个有
- `ImpactInt` —— 6/12 个有
- `easy float` —— 6/12 个有
- `FluxKontextImageScale` —— 4/12 个有
- `LoraLoaderModelOnly` —— 3/12 个有
- `YC Color Match` —— 2/12 个有
- `DuckHideNode` —— 1/12 个有
- `ImageSmartSharpen+` —— 1/12 个有
- `QwenMultiangleCameraNode` —— 1/12 个有
- `SaveImageAndMetadata_` —— 1/12 个有
- `easy positive` —— 1/12 个有
- `easy promptList` —— 1/12 个有

## 典型参数

无可统计的参数。

## 常见问题

参数体检未发现问题。

## 建议与风险

- 样本量不足且无参数可统计，暂无法归纳出可靠结论
