---
name: unknown_workflow_lora_sampler_clip_9
type: Unknown Workflow
frequency: 17
level: weak
coverage: 0.902647
common_nodes: [CLIPLoader, CLIPTextEncode, CLIPVisionEncode, CLIPVisionLoader, JWInteger, KSamplerAdvanced, LayerUtility: ImageScaleByAspectRatio V2, LoadImage, LoraLoaderModelOnly, ModelSamplingSD3, PathchSageAttentionKJ, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [视频生成/图生视频/1978096633571368961.json, 视频生成/图生视频/1978140653064445953.json, 视频生成/图生视频/1978111164158763009.json, 视频生成/图生视频/1976190699999756289.json, 视频生成/图生视频/1978095349178982402.json, 视频生成/图生视频/1972554470959869953.json, 视频生成/图生视频/1972558560423047170.json, 视频生成/图生视频/1978387992047931393.json, 视频生成/图生视频/1978282591151349762.json, 视频生成/图生视频/1985889345833971714.json, 视频生成/图生视频/1981669095458381825.json, 视频生成/图生视频/1985890821373341698.json, 视频生成/图生视频/1972577637715668993.json, 视频生成/图生视频/1975896909040758785.json, 视频生成/图生视频/2016122544050413569.json, 视频生成/图生视频/1976186558992793601.json, 视频生成/图生视频/1977433925884747777.json]
source: knowledge_consolidation
---

# unknown_workflow_lora_sampler_clip_9

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/1978096633571368961.json、视频生成/图生视频/1978140653064445953.json、视频生成/图生视频/1978111164158763009.json、视频生成/图生视频/1976190699999756289.json、视频生成/图生视频/1978095349178982402.json…）

- **类型**：Unknown Workflow
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 17 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `CLIPVisionEncode`
- `CLIPVisionLoader`
- `JWInteger`
- `KSamplerAdvanced`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `LoadImage`
- `LoraLoaderModelOnly`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CR Prompt Text` —— 16/17 个有
- `ImageFromBatch+` —— 16/17 个有
- `WanImageToVideo` —— 15/17 个有
- `TorchCompileModel` —— 14/17 个有
- `VHS_VideoCombine` —— 12/17 个有
- `SaveImage` —— 5/17 个有
- `TT_img_enc` —— 5/17 个有
- `WanFirstLastFrameToVideo` —— 2/17 个有
- `FSampler` —— 1/17 个有
- `FSamplerAdvanced` —— 1/17 个有
- `RIFE VFI` —— 1/17 个有
- `TT_img_enc_v2` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 17 | 65% |
| Prompt 约束强度(CFG) | 8 | 6 - 14 | 17 | 66% |
| 采样算法 | 1 | 1 - 3.5 | 17 | 34% |
| 调度器 | euler | - | 17 | 94% |
| 重绘幅度 | simple | - | 17 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，17 个样本，一致性 65%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 14，17 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，17 个样本，取值分散，一致性仅 34%
- 调度器 最常用 euler，17 个样本，一致性 94%
- 重绘幅度 最常用 simple，17 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 14，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
