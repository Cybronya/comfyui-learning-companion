---
name: unknown_workflow_video_sampler_clip_11
type: Unknown Workflow
frequency: 27
level: weak
coverage: 0.895778
common_nodes: [CLIPLoader, CLIPTextEncode, KSamplerAdvanced, LoadImage, ModelSamplingSD3, PathchSageAttentionKJ, SimpleMath+, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, WanImageToVideo, easy int]
problems: []
missing: []
members: [视频生成/图生视频/WAN2.2 图生视频(超强提示词版)_1955215890101014529.json, 视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json, 视频生成/图生视频/Wan2.2图生视频加速_1953037159256289282.json, 视频生成/图生视频/wan2.2 14B图生视频加速流_1955442912282775554.json, 视频生成/图生视频/wan2.2 14B图生视频｜KJ加速_1957271375608213506.json, 视频生成/图生视频/wan2.2 image to video 图生视频｜加速_1956923481642426370.json, 视频生成/图生视频/wan2.2 动态人物杂志海报｜加速版_1955447179764797442.json, 视频生成/图生视频/wan2.2 动态壁纸生成器 16FPS_1952614718961848322.json, 视频生成/图生视频/wan2.2 图生视频体验_1950070634309181442.json, 视频生成/图生视频/wan2.2 图生视频｜加速流_1955832796889714690.json, 视频生成/图生视频/wan2.2 图生视频｜极速版_1959200308658384898.json, 视频生成/图生视频/wan2.2 图生视频｜高清加速_1955505407994183681.json, 视频生成/图生视频/wan2.2 标准基础图生视频_1959201983930511361.json, 视频生成/图生视频/wan2.2 海报图生视频｜加速流_1959202864231034882.json, 视频生成/图生视频/wan2.2 视频动态海报｜1080P_1955506128698445825.json, 视频生成/图生视频/wan2.2 高清动态人物海报｜1080P版_1955448466613813249.json, 视频生成/图生视频/wan2.2 高级动态海报｜人物一致性_1955834523080691713.json, 视频生成/图生视频/wan2.2 高级动态海报｜高清1080P_1955835322741526529.json, 视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词_1949713099642294274.json, 视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词_2004402165575806978.json, 视频生成/图生视频/wan2.2-14B 官方图生视频+自动提示词（自动生成视频）_1983463880548655106.json, 视频生成/图生视频/wan2.2-14B图生视频加速流_1950029873998905345.json, 视频生成/图生视频/wan2.2-14B图生视频加速流_1952552254299680769.json, 视频生成/图生视频/wan2.2-14B图生视频加速流_1955503072236617730.json, 视频生成/图生视频/wan2.2-14B图生视频加速流_1955504798234656769.json, 视频生成/图生视频/wan2.2-14B图生视频加速流_1959204229682507777.json, 视频生成/图生视频/自己用：WAN2.2 图生视频_1955825577107210241.json]
source: knowledge_consolidation
---

# unknown_workflow_video_sampler_clip_11

> 由 `engine/knowledge_consolidation` 从 27 个 workflow 归纳得出（视频生成/图生视频/WAN2.2 图生视频(超强提示词版)_1955215890101014529.json、视频生成/图生视频/Wan2.2_14B_图生视频 (8步加速) + 提示词扩写_1952277132212948994.json、视频生成/图生视频/Wan2.2图生视频加速_1953037159256289282.json、视频生成/图生视频/wan2.2 14B图生视频加速流_1955442912282775554.json、视频生成/图生视频/wan2.2 14B图生视频｜KJ加速_1957271375608213506.json…）

- **类型**：Unknown Workflow
- **样本数**：27
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：90%

## 共有节点

全部 27 个 workflow 都包含：
- `CLIPLoader`
- `CLIPTextEncode`
- `KSamplerAdvanced`
- `LoadImage`
- `ModelSamplingSD3`
- `PathchSageAttentionKJ`
- `SimpleMath+`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `WanImageToVideo`
- `easy int`

**可变部分**（部分 workflow 才有）：
- `DF_Integer` —— 26/27 个有
- `LayerUtility: ImageScaleByAspectRatio V2` —— 26/27 个有
- `PrimitiveBoolean` —— 26/27 个有
- `easy cleanGpuUsed` —— 26/27 个有
- `easy showAnything` —— 26/27 个有
- `TextBox` —— 25/27 个有
- `CLIPVisionEncode` —— 24/27 个有
- `CLIPVisionLoader` —— 24/27 个有
- `RH_Captioner` —— 24/27 个有
- `easy ifElse` —— 24/27 个有
- `CR Text Replace` —— 23/27 个有
- `LayerUtility: PurgeVRAM V2` —— 22/27 个有
- `LoraLoaderModelOnly` —— 22/27 个有
- `LayerUtility: PurgeVRAM` —— 5/27 个有
- `PatchModelPatcherOrder` —— 5/27 个有
- `TorchCompileModelWanVideoV2` —— 5/27 个有
- `RHHiddenNodes` —— 2/27 个有
- `RH_Translator` —— 2/27 个有
- `ImageResizeKJv2` —— 1/27 个有
- `JjkText` —— 1/27 个有
- `QwenLoader` —— 1/27 个有
- `Textbox` —— 1/27 个有
- `WanVideoPromptExtender` —— 1/27 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | randomize | - | 27 | 85% |
| Prompt 约束强度(CFG) | 8 | 8 - 20 | 27 | 56% |
| 采样算法 | 1 | 1 - 4 | 27 | 28% |
| 调度器 | euler | - | 27 | 93% |
| 重绘幅度 | simple | - | 27 | 100% |

## 常见问题

参数体检未发现问题。

## 建议与风险

- 采样步数 最常用 randomize，27 个样本，一致性 85%
- Prompt 约束强度(CFG) 中位数 8，观测区间 8 - 20，27 个样本
- 采样算法 中位数 1，观测区间 1 - 4，27 个样本，取值分散，一致性仅 28%
- 调度器 最常用 euler，27 个样本，一致性 93%
- 重绘幅度 最常用 simple，27 个样本，一致性 100%
- 风险：Prompt 约束强度(CFG) 观测到 20，超出安全上限 12（CFG 偏高容易出现过度约束（如脸部异常、过饱和））
