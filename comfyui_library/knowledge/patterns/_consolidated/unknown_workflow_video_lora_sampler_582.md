---
name: unknown_workflow_video_lora_sampler_582
type: Unknown Workflow
frequency: 5
level: strong
coverage: 0.9592
common_nodes: [CLIPLoader, CLIPTextEncode, CR Prompt Text, GetVideoComponents, ImageConcanate, JWInteger, KSamplerAdvanced, LoadImage, LoadVideo, LoraLoaderModelOnly, ModelSamplingSD3, PDIMAGE_LongerSize, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, Wan22FunControlToVideo]
problems: []
missing: []
members: [平台全量/【Canny控制】视频风格转绘工作流_2062458006327087106.json, 平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json, 视频生成/图生视频/(官方)Wan 2.2 Fun Contorl 姿势控制加速稳定版V1_1956384459622940674.json, 视频生成/图生视频/（官方版）Wan Fun Control深度控制IP2V动作复刻V1_1956389723734507522.json, 视频生成/图生视频/（官方版）视频风格迁移Wan Fun Control线稿IP2V动作复刻V1_1956395513753030657.json]
source: knowledge_consolidation
---

# unknown_workflow_video_lora_sampler_582

> 由 `engine/knowledge_consolidation` 从 5 个 workflow 归纳得出（平台全量/【Canny控制】视频风格转绘工作流_2062458006327087106.json、平台全量/🦖Wan 2.2 Fun姿势控制_1957350483247689729.json、视频生成/图生视频/(官方)Wan 2.2 Fun Contorl 姿势控制加速稳定版V1_1956384459622940674.json、视频生成/图生视频/（官方版）Wan Fun Control深度控制IP2V动作复刻V1_1956389723734507522.json、视频生成/图生视频/（官方版）视频风格迁移Wan Fun Control线稿IP2V动作复刻V1_1956395513753030657.json）

- **类型**：Unknown Workflow
- **样本数**：5
- **可信度**：强结论
- **平均知识覆盖**：96%

## 共有节点

全部 5 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CR Prompt Text`
- `GetVideoComponents`
- `ImageConcanate`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadImage`
- `LoadVideo`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PDIMAGE_LongerSize`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `Wan22FunControlToVideo`

**可变部分**（部分 workflow 才有）：
- `Canny` —— 4/5 个有
- `SaveImage` —— 4/5 个有
- `DWPreprocessor` —— 2/5 个有
- `ACE_ImageGetSize` —— 1/5 个有
- `DepthAnything_V2` —— 1/5 个有
- `DownloadAndLoadDepthAnythingV2Model` —— 1/5 个有
- `ImageResizeKJv2` —— 1/5 个有
- `RH_Captioner` —— 1/5 个有
- `ResizeLongestToNode` —— 1/5 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 5 | 80% |
| Prompt 约束强度(CFG) | 4 | 4 - 4 | 5 | 100% |
| 采样算法 | 1 | 1 - 1 | 5 | 100% |
| 调度器 | euler | - | 5 | 100% |
| 重绘幅度 | simple | - | 5 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，5 个样本，一致性 80%
- Prompt 约束强度(CFG) 中位数 4，观测区间 4 - 4，5 个样本，取值集中（一致性 100%）
- 采样算法 中位数 1，观测区间 1 - 1，5 个样本，取值集中（一致性 100%）
- 调度器 最常用 euler，5 个样本，一致性 100%
- 重绘幅度 最常用 simple，5 个样本，一致性 100%
