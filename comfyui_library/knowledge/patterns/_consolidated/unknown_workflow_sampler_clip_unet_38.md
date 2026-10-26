---
name: unknown_workflow_sampler_clip_unet_38
type: Unknown Workflow
frequency: 18
level: weak
coverage: 0.905833
common_nodes: [CLIPLoader, CLIPTextEncode, JWInteger, KSamplerAdvanced, LoadImage, ModelSamplingSD3, UNETLoader, VAEDecode, VAELoader]
problems: []
missing: []
members: [图片生成/图生图/wan2.2i2v_1949827162749714433.json, 视频生成/图生视频/(10+4官方版)Wan2.2 Fsampler噪声预测H2S2高动态图生视频v2（25%加速版）_1978096633571368961.json, 视频生成/图生视频/(2+4官方版)Wan2.2 Moe Lightx2v新版高噪模型高动态图生视频v1（超级加速）_1978140653064445953.json, 视频生成/图生视频/(4+4官方版)Wan2.2 Moe Lightx2v新版高噪模型高动态图生视频v1_1978111164158763009.json, 视频生成/图生视频/(光鸟-官方版10+4)Wan2.2差异加速高动态图生视频v2（慢速版）_1976190699999756289.json, 视频生成/图生视频/(官方版10+4)Wan2.2差异加速高动态图生视频v2（慢速版）_1978095349178982402.json, 视频生成/图生视频/(官方版10+6)Wan2.2差异加速高动态图生视频v2（慢速版）_1972554470959869953.json, 视频生成/图生视频/(官方版4+4)Wan2.2图生视频v1_1972558560423047170.json, 视频生成/图生视频/90秒81帧6步超极速图生视频_1995392959409479682.json, 视频生成/图生视频/Wan2.2 Moe Lightx2v图生视频v1_1978387992047931393.json, 视频生成/图生视频/Wan2.2 Moe Lightx2v新版高噪模型高动态首尾帧视频v1_1978282591151349762.json, 视频生成/图生视频/图生视频 Wan2.2 Moe Lightx2v_1985889345833971714.json, 视频生成/图生视频/首尾帧生成（Wan2.2-Moe+Lightx2v加速）_1985890821373341698.json, 视频生成/图生视频/（CHB V3（自用））运动增强图生视频V4（官方流，不支持KJ）_1972577637715668993.json, 视频生成/图生视频/（CLK V2.1（自用））N版运动增强图生视频V1（官方流，不支持KJ）_1975896909040758785.json, 视频生成/图生视频/（本地解码）N SFW 破 限 Dyno Remix I2V 模型图生视频 V1（动态加强）_2016122544050413569.json, 视频生成/图生视频/（自用）Dyno Remix I2V 0.6模型图生视频V1（官方流）_1976186558992793601.json, 视频生成/图生视频/（自用）Dyno Remix I2V 0.8模型图生视频V2（官方流）_1977433925884747777.json]
source: knowledge_consolidation
---

# unknown_workflow_sampler_clip_unet_38

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（图片生成/图生图/wan2.2i2v_1949827162749714433.json、视频生成/图生视频/(10+4官方版)Wan2.2 Fsampler噪声预测H2S2高动态图生视频v2（25%加速版）_1978096633571368961.json、视频生成/图生视频/(2+4官方版)Wan2.2 Moe Lightx2v新版高噪模型高动态图生视频v1（超级加速）_1978140653064445953.json、视频生成/图生视频/(4+4官方版)Wan2.2 Moe Lightx2v新版高噪模型高动态图生视频v1_1978111164158763009.json、视频生成/图生视频/(光鸟-官方版10+4)Wan2.2差异加速高动态图生视频v2（慢速版）_1976190699999756289.json…）

- **类型**：Unknown Workflow
- **样本数**：18
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：91%

## 共有节点

全部 18 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `JWInteger`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `CLIPVisionEncode` —— 17/18 个有
- `CLIPVisionLoader` —— 17/18 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 17/18 个有
- `LoraLoaderModelOnly` —— 17/18 个有
- `PathchSageAttentionKJ` —— 17/18 个有
- `CR Prompt Text` —— 16/18 个有
- `ImageFromBatch+` —— 16/18 个有
- `WanImageToVideo` —— 16/18 个有
- `TorchCompileModel` —— 14/18 个有
- `VHS_VideoCombine` —— 13/18 个有
- `SaveImage` —— 5/18 个有
- `TT_img_enc` —— 5/18 个有
- `LayerUtility: PurgeVRAM` —— 2/18 个有
- `WanFirstLastFrameToVideo` —— 2/18 个有
- `FSampler` —— 1/18 个有
- `FSamplerAdvanced` —— 1/18 个有
- `RIFE VFI` —— 1/18 个有
- `TT_img_enc_v2` —— 1/18 个有
- `TextBox` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | fixed | - | 18 | 61% |
| Prompt 约束强度(CFG) | 8 | 6 - 20 | 18 | 58% |
| 采样算法 | 1 | 1 - 3.5 | 18 | 33% |
| 调度器 | euler | - | 18 | 94% |
| 重绘幅度 | simple | - | 18 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 fixed，18 个样本，一致性 61%
- Prompt 约束强度(CFG) 中位数 8，观测区间 6 - 20，18 个样本
- 采样算法 中位数 1，观测区间 1 - 3.5，18 个样本，取值分散，一致性仅 33%
- 调度器 最常用 euler，18 个样本，一致性 94%
- 重绘幅度 最常用 simple，18 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
