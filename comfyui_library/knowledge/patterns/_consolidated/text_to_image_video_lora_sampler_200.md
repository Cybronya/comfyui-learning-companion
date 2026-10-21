---
name: text_to_image_video_lora_sampler_200
type: Text To Image
frequency: 2
level: weak
coverage: 0.912
common_nodes: [CFGNorm, CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, DownloadAndLoadGIMMVFIModel, EmptyLatentImage, FSamplerAdvanced, GIMMVFI_interpolate, ImageResizeKJv2, Int, JjkText, KSampler, LayerUtility: PurgeVRAM V2, LoadImage, LoraLoaderModelOnly, ModelPatchTorchSettings, PathchSageAttentionKJ, PrimitiveString, PrimitiveStringMultiline, RHHiddenNodes, ShowText|pysssss, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, solarL_SaveImagesToZip, wanBlockSwap, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/AI漫剧Wan22角色表演图生视频｜FSampler+LLM动态可控｜官方版稳定运行_2104783563366424577.json, 视频生成/图生视频/Wan22+FSampler+LLM漫剧图生视频｜超高动态可控官方版｜角色表演鲜活_2104777184400470018.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_200

> 由 `engine/knowledge_consolidation` 从 2 个 workflow 归纳得出（视频生成/图生视频/AI漫剧Wan22角色表演图生视频｜FSampler+LLM动态可控｜官方版稳定运行_2104783563366424577.json、视频生成/图生视频/Wan22+FSampler+LLM漫剧图生视频｜超高动态可控官方版｜角色表演鲜活_2104777184400470018.json）

- **类型**：Text To Image
- **样本数**：2
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 2 个 workflow 都包含：
- `CFGNorm`
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `DownloadAndLoadGIMMVFIModel`
- `EmptyLatentImage`
- `FSamplerAdvanced`
- `GIMMVFI_interpolate`
- `ImageResizeKJv2`
- `Int`
- `JjkText`
- `KSampler`
- `LayerUtility: PurgeVRAM V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelPatchTorchSettings`
- `PathchSageAttentionKJ`
- `PrimitiveString`
- `PrimitiveStringMultiline`
- `RHHiddenNodes`
- `ShowText|pysssss`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `solarL_SaveImagesToZip`
- `wanBlockSwap`
- `孤海注释`

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| Prompt 约束强度(CFG) | 4.5 | - | 2 | 100% |
| 重绘幅度 | 1 | - | 2 | 100% |
| 高度 | 80 | - | 2 | 100% |
| 采样算法 | er_sde | - | 2 | 100% |
| 调度器 | beta | - | 2 | 100% |
| 采样步数 | 4 | - | 2 | 100% |
| 宽度 | 80 | - | 2 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 2/2 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- Prompt 约束强度(CFG) 中位数 4.5，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 重绘幅度 中位数 1，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，2 个样本，一致性 100%
- 调度器 最常用 beta，2 个样本，一致性 100%
- 采样步数 中位数 4，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，样本不足，未给区间，2 个样本，取值集中（一致性 100%）
- 高发问题（2/2 个样本）：Steps较低可能导致细节不足
- 注意：仅 2 个样本，上述结论仅供参考，建议积累到 5 个以上再据此调参
