---
name: unknown_workflow_sampler_clip_unet_85
type: Unknown Workflow
frequency: 12
level: weak
coverage: 0.98225
common_nodes: [CLIPLoader, CLIPTextEncode, EmptyHunyuanLatentVideo, KSamplerAdvanced, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json, 视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json, 视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json, 视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json, 视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json, 视频生成/文生视频/Wan2.2 Dyno+Remix 新模型1.0文生视频V2（官方采样器）_1975847969142517762.json, 视频生成/文生视频/Wan2.2 Dyno+Remix文生视频V1_1974792612945244161.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2同模型高动态文生视频V1（官方采样器）_1979857088648220673.json, 视频生成/文生视频/（6+4步）Wan2.2 Smooth Mix V2差异模型高动态文生视频V1（官方采样器）_1979868052277858305.json, 视频生成/文生视频/（6+6步）Wan2.2 Smooth Mix高动态文生视频V1（官方采样器）_1978740895153541121.json, 视频生成/文生视频/（自用）Dyno+Remix 1.0新模型文生视频（官方版）_1975846179902722050.json, 视频生成/文生视频/（自用）Dyno+Remix文生视频（官方版）_1974785719120080898.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_85

> 由 `engine/knowledge_consolidation` 从 12 个 workflow 归纳得出（视频生成/文生视频/DNR-wan2.2-官方文生视频_1952913163996041218.json、视频生成/文生视频/Holocine——Wan2.2连续多分镜长视频生成_1982455092706197505.json、视频生成/文生视频/Holocine电影分镜工作流_1982118673722818561.json、视频生成/文生视频/Holocine电影分镜工作流（含提示词样例）_1987110613501587458.json、视频生成/文生视频/Wan2.2 14B+LightX2V 8倍加速文生视频工作流_1950043620181237761.json…）

- **类型**：Unknown Workflow
- **样本数**：12
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：98%

## 共有节点

全部 12 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `EmptyHunyuanLatentVideo`
- `KSamplerAdvanced`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `INTConstant` —— 10/12 个有
- `VHS_VideoCombine` —— 10/12 个有
- `LoraLoaderModelOnly` —— 9/12 个有
- `JWInteger` —— 8/12 个有
- `SaveImage` —— 7/12 个有
- `TT_img_enc` —— 7/12 个有
- `ImageFromBatch+` —— 4/12 个有
- `easy cleanGpuUsed` —— 4/12 个有
- `LoadImage` —— 2/12 个有
- `LayerUtility: PurgeVRAM` —— 1/12 个有
- `SeargePromptText` —— 1/12 个有
- `TextBox` —— 1/12 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 12 | 75% |
| Prompt 约束强度(CFG) | 12 | 8 - 20 | 12 | 71% |
| 采样算法 | 1 | 1 - 3.5 | 12 | 36% |
| 调度器 | euler | - | 12 | 75% |
| 重绘幅度 | simple | - | 12 | 83% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，12 个样本，一致性 75%
- Prompt 约束强度(CFG) 中位数 12，观测区间 8 - 20，12 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，12 个样本，取值分散，一致性仅 36%
- 调度器 最常用 euler，12 个样本，一致性 75%
- 重绘幅度 最常用 simple，12 个样本，一致性 83%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
