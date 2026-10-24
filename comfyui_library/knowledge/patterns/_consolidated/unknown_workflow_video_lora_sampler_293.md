---
name: unknown_workflow_video_lora_sampler_293
type: Unknown Workflow
frequency: 7
level: strong
coverage: 0.918
common_nodes: [CLIPLoader, CLIPTextEncode, ImageConcanate, KSamplerAdvanced, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine]
problems: []
missing: []
members: [视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Contorl 姿势控制加速稳定版V1_1956384459622940674.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1996850315431485442.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1_1956358088464977921.json, 视频生成/图生视频/【官版】Wan2.2 14B Fun Control 多模态控制_1956635710498246657.json, 视频生成/图生视频/（官方版）Wan Fun Control深度控制IP2V动作复刻V1_1956389723734507522.json, 视频生成/图生视频/（官方版）视频风格迁移Wan Fun Control线稿IP2V动作复刻V1_1956395513753030657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_293

> 由 `engine/knowledge_consolidation` 从 7 个 workflow 归纳得出（视频生成/图生视频/(头发生长过程)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1998571771651588098.json、视频生成/图生视频/(官方)Wan 2.2 Fun Contorl 姿势控制加速稳定版V1_1956384459622940674.json、视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1 浮云_1996850315431485442.json、视频生成/图生视频/(官方)Wan 2.2 Fun Inp首尾帧加速稳定版V1_1956358088464977921.json、视频生成/图生视频/【官版】Wan2.2 14B Fun Control 多模态控制_1956635710498246657.json…）

- **类型**：Unknown Workflow
- **样本数**：7
- **可信度**：强结论
- **平均知识覆盖**：92%

## 共有节点

全部 7 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `ImageConcanate`
- `KSamplerAdvanced`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 6/7 个有
- `JWInteger` —— 6/7 个有
- `PDIMAGE_LongerSize` —— 6/7 个有
- `CreateVideo` —— 4/7 个有
- `GetVideoComponents` —— 4/7 个有
- `LoadVideo` —— 4/7 个有
- `SaveVideo` —— 4/7 个有
- `Wan22FunControlToVideo` —— 4/7 个有
- `Canny` —— 3/7 个有
- `SaveImage` —— 3/7 个有
- `WanFunInpaintToVideo` —— 3/7 个有
- `DWPreprocessor` —— 2/7 个有
- `DepthAnything_V2` —— 1/7 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/7 个有
- `PreviewImage` —— 1/7 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 7 | 86% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 7 | 100% |
| 采样算法 | 1 | 1 - 1 | 7 | 100% |
| 调度器 | euler | - | 7 | 100% |
| 重绘幅度 | simple | - | 7 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，7 个样本，一致性 86%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，7 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，7 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，7 个样本，一致性 100%
- 重绘幅度 最常用 simple，7 个样本，一致性 100%
