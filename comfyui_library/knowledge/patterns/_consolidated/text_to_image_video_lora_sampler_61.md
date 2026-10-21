---
name: text_to_image_video_lora_sampler_61
type: Text To Image
frequency: 11
level: strong
coverage: 0.538364
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, GetNode, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3MemoryEfficientSageAttentionPatch, MiniMaxH3ReferenceToVideo, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, SetNode, UNETLoader, VAEDecode, VAEDecodeAudio, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/探店商品视频无滤镜版｜MiniMax+H3数字人生成_2093789772853633025.json, 视频生成/图生视频/AITUDOU H3 Skill2.0全能参考版｜单采直出视频_2098755113656610818.json, 视频生成/图生视频/H3多参考生视频优化版 高质量图生视频工具_2099586599930646530.json, 视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099220276063068161.json, 视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099597584175292417.json, 视频生成/图生视频/H3多图参考2K高清工作流 9图参考低显存加速_2099565414308208641.json, 视频生成/图生视频/MiniMax H3全栈式短剧多图参考自动生成二采提示词自动优化版V2.0_2109368887719587842.json, 视频生成/图生视频/MiniMax H3多图参考2K高清图生视频处理工作流_2101011461173760002.json, 视频生成/图生视频/MiniMax H3多图参考2K高清工作流 9图参考低显存加速_2099199366883012609.json, 视频生成/图生视频/minimax h3多图参考2K高清工作流｜写实运镜图生视频_2100796636741070849.json, 视频生成/文生视频/MiniMax-H3 全栈式短剧 V1.0｜多图音频参考二采优化_2096882058416189442.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_61

> 由 `engine/knowledge_consolidation` 从 11 个 workflow 归纳得出（数字人/数字人/探店商品视频无滤镜版｜MiniMax+H3数字人生成_2093789772853633025.json、视频生成/图生视频/AITUDOU H3 Skill2.0全能参考版｜单采直出视频_2098755113656610818.json、视频生成/图生视频/H3多参考生视频优化版 高质量图生视频工具_2099586599930646530.json、视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099220276063068161.json、视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099597584175292417.json…）

- **类型**：Text To Image
- **样本数**：11
- **可信度**：强结论
- **平均知识覆盖**：54%

## 共有节点

全部 11 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `GetNode`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3MemoryEfficientSageAttentionPatch`
- `MiniMaxH3ReferenceToVideo`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `SetNode`
- `UNETLoader`
- `VAEDecode`
- `VAEDecodeAudio`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `PrimitiveFloat` —— 10/11 个有
- `SplitSigmas` —— 10/11 个有
- `LTXVConcatAVLatent` —— 9/11 个有
- `LTXVSeparateAVLatent` —— 9/11 个有
- `MinimaxH3LatentUpscaler3D` —— 9/11 个有
- `easy float` —— 9/11 个有
- `PrimitiveStringMultiline` —— 7/11 个有
- `SaveImage` —— 7/11 个有
- `VHS_LoadVideo` —— 7/11 个有
- `llama_cpp_instruct_adv` —— 7/11 个有
- `llama_cpp_model_loader` —— 7/11 个有
- `llama_cpp_parameters` —— 7/11 个有
- `Any Switch (rgthree)` —— 6/11 个有
- `Fast Groups Bypasser (rgthree)` —— 6/11 个有
- `PurgeVRAM_UTK` —— 6/11 个有
- `easy showAnything` —— 6/11 个有
- `LoadAudio` —— 5/11 个有
- `ModelAttentionBackend` —— 4/11 个有
- `PrimitiveBoolean` —— 4/11 个有
- `Text` —— 4/11 个有
- `UniBlockSwap` —— 4/11 个有
- `VHS_LoadAudioUpload` —— 4/11 个有
- `easy ifElse` —— 4/11 个有
- `ShowText|pysssss` —— 3/11 个有
- `StringConcatenate` —— 3/11 个有
- `GetImage` —— 2/11 个有
- `ImageScale` —— 2/11 个有
- `JoinStringMulti` —— 2/11 个有
- `PreviewImage` —— 2/11 个有
- `PrimitiveInt` —— 2/11 个有
- `TextGenerate` —— 2/11 个有
- `ToString` —— 2/11 个有
- `YUAN_TXTJsonExtractor` —— 2/11 个有
- `YUAN_TXTParagraphSplitter` —— 2/11 个有
- `YUAN_TXTShotReplace` —— 2/11 个有
- `YuanAudioList` —— 2/11 个有
- `YuanAudioSplit` —— 2/11 个有
- `YuanMultiImage` —— 2/11 个有
- `YuanTool` —— 2/11 个有
- `AudioSeparation` —— 1/11 个有
- `BatchImagesNode` —— 1/11 个有
- `Float` —— 1/11 个有
- `TrimAudioDuration` —— 1/11 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 采样步数 | 4 | 4 - 4 | 11 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 11 | 100% |
| 采样算法 | er_sde | - | 11 | 100% |
| 调度器 | beta | - | 11 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 11 | 100% |
| 宽度 | 80 | 80 - 80 | 11 | 100% |
| 高度 | 80 | 80 - 80 | 11 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 11/11 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 采样步数 中位数 4，观测区间 4 - 4，11 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，11 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，11 个样本，一致性 100%
- 调度器 最常用 beta，11 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，11 个样本，取值集中（一致性 100%）
- 宽度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，11 个样本，取值集中（一致性 100%）
- 高发问题（11/11 个样本）：Steps较低可能导致细节不足
