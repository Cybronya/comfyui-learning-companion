---
name: text_to_image_lora_sampler_clip_55
type: Text To Image
frequency: 17
level: weak
coverage: 0.884882
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, CreateVideo, EmptyLatentImage, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, PrimitiveFloat, RandomNoise, SamplerCustomAdvanced, SaveVideo, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader]
problems: [Steps较低可能导致细节不足]
missing: []
members: [视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json, 视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json, 视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json, 视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频_2089024944066883586.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频视频生视频多素材融合_2088699208495882241.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2092760928600285186.json, 视频生成/图生视频/多图参考生视频｜MINIMAX-H3视频生视频直出_2093795328280584193.json, 视频生成/图生视频/多图生视频+音频+视频接入｜MiniMax H3场景特效_2092205364438720514.json, 视频生成/图生视频/多图生视频音频视频接入｜MiniMax H3场景特效生成_2092018470065106945.json, 视频生成/图生视频/官流直出美少女视频｜Minimax-H3 图生视频原汁原味_2096269567709499393.json, 视频生成/图生视频/实用四合一工作流：Qwen文生图、2511图生图；MinMax首尾视频、MinMax多图视频_2110212930481508354.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093430390005518337.json, 视频生成/图生视频/开源加速版图生视频｜MiniMax-H3角色一致性设计_2093761824507383810.json, 视频生成/图生视频/音画同步参考工作流｜MiniMax H3角色表演图生视频_2091604729305583617.json, 视频生成/图生视频/音画同步参考生成｜MiniMax H3角色表演图生视频_2091775715330060290.json]
source: knowledge_consolidation
---

# text_to_image_lora_sampler_clip_55

> 由 `engine/knowledge_consolidation` 从 17 个 workflow 归纳得出（视频生成/图生视频/四合一全家桶｜Qwen文生图+2511图生图+MiniMax首尾帧与多图视频_2111275974745743362.json、视频生成/图生视频/图生视频加速版｜MiniMax H3人物场景特效生成_2093842351939743746.json、视频生成/图生视频/多参考图生视频｜MiniMax_H3可本地运行场景特效_2089811445595860993.json、视频生成/图生视频/多图参考生视频｜MINIMAX H3 多图融合出片_2089280249723973634.json、视频生成/图生视频/多图参考生视频｜MINIMAX-H3图生视频生成工作流_2095075446797979649.json…）

- **类型**：Text To Image
- **样本数**：17
- **可信度**：弱结论（样本不足）
- **平均知识覆盖**：88%

## 共有节点

全部 17 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `CreateVideo`
- `EmptyLatentImage`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `PrimitiveFloat`
- `RandomNoise`
- `SamplerCustomAdvanced`
- `SaveVideo`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`

**可变部分**（部分 workflow 才有）：
- `JjkText` —— 16/17 个有
- `ResolutionSelector` —— 16/17 个有
- `solarL_SaveImagesToZip` —— 16/17 个有
- `孤海注释` —— 16/17 个有
- `MiniMaxH3ReferenceToVideo` —— 15/17 个有
- `PrimitiveStringMultiline` —— 14/17 个有
- `LoadAudio` —— 10/17 个有
- `MiniMaxH3ImageToVideo` —— 4/17 个有
- `PathchSageAttentionKJ` —— 3/17 个有
- `ConditioningZeroOut` —— 2/17 个有
- `GetImageSize` —— 2/17 个有
- `GetVideoComponents` —— 2/17 个有
- `ImageScaleToTotalPixels` —— 2/17 个有
- `LatentUpscale` —— 2/17 个有
- `LoadVideo` —— 2/17 个有
- `ModelPatchTorchSettings` —— 2/17 个有
- `SaveImage` —— 2/17 个有
- `SpectrumSDXLBatch` —— 2/17 个有
- `TextEncodeQwenImageEditPlus` —— 2/17 个有
- `VAEEncode` —— 2/17 个有
- `Label (rgthree)` —— 1/17 个有
- `MiniMaxH3SigmaShift` —— 1/17 个有
- `ResizeImageMaskNode` —— 1/17 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 9 | 17 | 73% |
| Prompt 约束强度(CFG) | 4.5 | 1 - 4.5 | 17 | 81% |
| 采样算法 | er_sde | - | 17 | 94% |
| 调度器 | beta | - | 17 | 94% |
| 重绘幅度 | 1 | 1 - 1 | 17 | 100% |
| 宽度 | 80 | 80 - 1080 | 17 | 0% |
| 高度 | 80 | 80 - 1920 | 17 | 0% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 20/17 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 9，17 个样本
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 1 - 4.5，17 个样本，取值集中（一致性 81%）
- 采样算法 最常用 er_sde，17 个样本，一致性 94%
- 调度器 最常用 beta，17 个样本，一致性 94%
- 重绘幅度 中位数 1，观测区间 1 - 1，17 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 1080，17 个样本，取值分散，一致性仅 0%
- 高度 中位数 80，观测区间 80 - 1920，17 个样本，取值分散，一致性仅 0%
- 高发问题（20/17 个样本）：Steps较低可能导致细节不足
