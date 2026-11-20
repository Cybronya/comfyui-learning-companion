---
name: unknown_workflow_sampler_unet_vae_209
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.825714
common_nodes: [CLIPVisionLoader, ComfySwitchNode, InvertMask, JoinImageWithAlpha, KSampler, LoadBackgroundRemovalModel, LoadImage, RemoveBackground, SaveGLB, SplatToFile3D, SplatToMesh, TripoSplatConditioning, TripoSplatPreprocessImage, TripoSplatSamplingPreview, UNETLoader, VAEDecodeTripoSplat, VAELoader]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [平台全量/3d_triposplat图生3D模型工作流_2081992045354373121.json, 平台全量/Tripo-单图生3D模型开源纯RH币_2067452323688964097.json, 平台全量/Triposplat 3D 高斯泼溅生成模型标准版_2073624234370363394.json, 平台全量/Triposplat 3D 高斯泼溅生成模型标准版_2075837209818779650.json, 平台全量/krea2-图转三维_2094627682339348481.json, 平台全量/triposplat_2075598937486086146.json, 视频生成/图生视频/3d_triposplat_image_to_gaussian_splat_2064180168951943169.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_unet_vae_209

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（平台全量/3d_triposplat图生3D模型工作流_2081992045354373121.json、平台全量/Tripo-单图生3D模型开源纯RH币_2067452323688964097.json、平台全量/Triposplat 3D 高斯泼溅生成模型标准版_2073624234370363394.json、平台全量/Triposplat 3D 高斯泼溅生成模型标准版_2075837209818779650.json、平台全量/krea2-图转三维_2094627682339348481.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：83%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPVisionLoader`
- `ComfySwitchNode`
- `InvertMask`
- `JoinImageWithAlpha`
- `KSampler`
- `LoadBackgroundRemovalModel`
- `LoadImage`
- `RemoveBackground`
- `SaveGLB`
- `SplatToFile3D`
- `SplatToMesh`
- `TripoSplatConditioning`
- `TripoSplatPreprocessImage`
- `TripoSplatSamplingPreview`
- `UNETLoader`
- `VAEDecodeTripoSplat`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CreateCameraInfo` —— 6/7 个有
- `CreateVideo` —— 6/7 个有
- `PreviewImage` —— 6/7 个有
- `RenderSplat` —— 6/7 个有
- `SaveVideo` —— 6/7 个有
- `SaveImage` —— 2/7 个有
- `Fast Groups Muter (rgthree)` —— 1/7 个有
- `Label (rgthree)` —— 1/7 个有
- `RMBG` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 20 | 20 - 20 | 7 | 100% |
| Prompt 约束强度(CFG) | 3 | 3 - 3 | 7 | 100% |
| 采样算法 | dpmpp_2m | - | 7 | 100% |
| 调度器 | simple | - | 7 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 7 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 7/7 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 采样步数 中位数 20，观测区间 20 - 20，7 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 3，观测区间 3 - 3，7 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_2m，7 个样本，一致性 100%
- 调度器 最常用 simple，7 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 高发问题（7/7 个样本）：发现KSampler但没有VAEDecode
