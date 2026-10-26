---
name: unknown_workflow_video_sampler_clip_243
type: Unknown Workflow
frequency: 2
level: weak
coverage: 0.828
common_nodes: [AudioCombine, CLIPLoader, CLIPTextEncode, CheckpointLoaderSimple, Compare, DF_Get_image_size, EmptyLatentAudio, Evaluate Integers, ImageResize+, Int, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoadWanVideoT5TextEncoder, MMAudioFeatureUtilsLoader, MMAudioModelLoader, MMAudioSampler, MathExpression|pysssss, Note _O, PreviewAudio, PreviewImage, RH_Captioner, RH_LLMAPI_NODE, SaveAudio, VAEDecodeAudio, VHS_VideoCombine, WanVideoBlockSwap, WanVideoDecode, WanVideoModelLoader, WanVideoSampler, WanVideoTextEncode, WanVideoTorchCompileSettings, WanVideoVACEEncode, WanVideoVACEModelSelect, WanVideoVACEStartToEndFrame, WanVideoVAELoader, easy ifElse, easy showAnything]
problems: [发现KSampler但没有VAEDecode]
missing: []
members: [视频生成/图生视频/VACE 14B-首尾帧视频_1927967408303292418.json, 视频生成/图生视频/VACE 14B-首尾帧视频_1929705242345246721.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_243

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/VACE 14B-首尾帧视频_1927967408303292418.json、视频生成/图生视频/VACE 14B-首尾帧视频_1929705242345246721.json）

- **类型**：Unknown Workflow
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：83%

## 共有节点

全部 2 个 workflow 都包含：
- `AudioCombine`
- `CLIPLoader`
- `CLIPTextEncode`
- `CheckpointLoaderSimple`
- `Compare`
- `DF_Get_image_size`
- `EmptyLatentAudio`
- `Evaluate Integers`
- `ImageResize+`
- `Int`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoadWanVideoT5TextEncoder`
- `MMAudioFeatureUtilsLoader`
- `MMAudioModelLoader`
- `MMAudioSampler`
- `MathExpression|pysssss`
- `Note _O`
- `PreviewAudio`
- `PreviewImage`
- `RH_Captioner`
- `RH_LLMAPI_NODE`
- `SaveAudio`
- `VAEDecodeAudio`
- `VHS_VideoCombine`
- `WanVideoBlockSwap`
- `WanVideoDecode`
- `WanVideoModelLoader`
- `WanVideoSampler`
- `WanVideoTextEncode`
- `WanVideoTorchCompileSettings`
- `WanVideoVACEEncode`
- `WanVideoVACEModelSelect`
- `WanVideoVACEStartToEndFrame`
- `WanVideoVAELoader`
- `easy ifElse`
- `easy showAnything`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 40 | - | 2 | 100% |
| 高度 | 1 | - | 2 | 100% |
| 采样步数 | 60 | - | 2 | 100% |
| Prompt 约束强度(CFG) | 7 | - | 2 | 100% |
| 采样算法 | dpmpp_3m_sde_gpu | - | 2 | 100% |
| 调度器 | exponential | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| 发现KSampler但没有VAEDecode | 2/2 | high | 发现KSampler但没有VAEDecode → 添加VAEDecode完成latent转换 |

## 建议与风险

- 宽度 中位数 40，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样步数 中位数 60，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 7，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 dpmpp_3m_sde_gpu，2 个样本，一致性 100%
- 调度器 最常用 exponential，2 个样本，一致性 100%
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：发现KSampler但没有VAEDecode
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
