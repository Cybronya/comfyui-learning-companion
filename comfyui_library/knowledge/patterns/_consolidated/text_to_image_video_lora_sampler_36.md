---
name: text_to_image_video_lora_sampler_36
type: Text To Image
frequency: 18
level: strong
coverage: 0.655556
common_nodes: [BasicGuider, BasicScheduler, CLIPLoader, CLIPTextEncode, ComfyMathExpression, EmptyLatentImage, JjkText, KSampler, KSamplerSelect, LoadImage, LoraLoaderModelOnly, MiniMaxH3ReferenceToVideo, PrimitiveFloat, RandomNoise, ResolutionSelector, SamplerCustomAdvanced, UNETLoader, VAEDecode, VAELoader, VHS_VideoCombine, solarL_SaveImagesToZip, 孤海注释]
problems: [Steps较低可能导致细节不足]
missing: []
members: [数字人/数字人/MiniMax-H3开源数字人全自动｜电商产品讲解虚拟主播_2111812476277972994.json, 数字人/数字人/MiniMax-H3开源数字人自动版，唱歌说唱口播电商讲解_2111912691190288386.json, 数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播带货_2111783890280083457.json, 数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解_2090069695356563458.json, 数字人/数字人/MiniMax-H3开源数字人，唱歌口播虚拟主播自动版_2111919197029748738.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜_2091171813098344450.json, 视频生成/图生视频/15秒卡点混剪｜MiniMaxH3转场特效视频运镜图生视频_2091249300000034818.json, 视频生成/图生视频/15秒卡点混剪｜MinimaxH3像素幻想Lab转场特效_2090885714388013057.json, 视频生成/图生视频/H3多参考生视频优化版 高质量图生视频工具_2099586599930646530.json, 视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099220276063068161.json, 视频生成/图生视频/H3多参考生视频优化版9图全开 多图参考高质量生成_2099597584175292417.json, 视频生成/图生视频/H3多图参考2K高清工作流 9图参考低显存加速_2099565414308208641.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版 高质量图生视频工具_2099190175938207745.json, 视频生成/图生视频/MiniMax H3多参考生视频优化版｜多图参考更听话，画面更贴需求_2099467720621387777.json, 视频生成/图生视频/MiniMax H3多参考生视频工作流，图生视频多素材融合方案_2103581304431407106.json, 视频生成/图生视频/MiniMax H3多图参考2K高清图生视频处理工作流_2101011461173760002.json, 视频生成/图生视频/MiniMax H3多图参考2K高清工作流 9图参考低显存加速_2099199366883012609.json, 视频生成/图生视频/minimax h3多图参考2K高清工作流｜写实运镜图生视频_2100796636741070849.json]
source: knowledge_consolidation
---

# text_to_image_video_lora_sampler_36

> 由 `engine/knowledge_consolidation` 从 18 个 workflow 归纳得出（数字人/数字人/MiniMax-H3开源数字人全自动｜电商产品讲解虚拟主播_2111812476277972994.json、数字人/数字人/MiniMax-H3开源数字人自动版，唱歌说唱口播电商讲解_2111912691190288386.json、数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播带货_2111783890280083457.json、数字人/数字人/MiniMax-H3开源数字人自动版｜唱歌说唱口播虚拟主播电商讲解_2090069695356563458.json、数字人/数字人/MiniMax-H3开源数字人，唱歌口播虚拟主播自动版_2111919197029748738.json…）

- **类型**：Text To Image
- **样本数**：18
- **可信度**：强结论
- **平均知识覆盖**：66%

## 共有节点

全部 18 个 workflow 都包含：
- `BasicGuider`
- `BasicScheduler`
- `CLIPLoader`
- `CLIPTextEncode`
- `ComfyMathExpression`
- `EmptyLatentImage`
- `JjkText`
- `KSampler`
- `KSamplerSelect`
- `LoadImage`
- `LoraLoaderModelOnly`
- `MiniMaxH3ReferenceToVideo`
- `PrimitiveFloat`
- `RandomNoise`
- `ResolutionSelector`
- `SamplerCustomAdvanced`
- `UNETLoader`
- `VAEDecode`
- `VAELoader`
- `VHS_VideoCombine`
- `solarL_SaveImagesToZip`
- `孤海注释`

**可变部分**（部分 workflow 才有）：
- `llama_cpp_instruct_adv` —— 16/18 个有
- `llama_cpp_model_loader` —— 16/18 个有
- `llama_cpp_parameters` —— 16/18 个有
- `GetNode` —— 15/18 个有
- `SetNode` —— 15/18 个有
- `VAEDecodeAudio` —— 13/18 个有
- `ModelAttentionBackend` —— 12/18 个有
- `LoadAudio` —— 11/18 个有
- `ShowText|pysssss` —— 11/18 个有
- `LTXVConcatAVLatent` —— 10/18 个有
- `LTXVSeparateAVLatent` —— 10/18 个有
- `MiniMaxH3MemoryEfficientSageAttentionPatch` —— 10/18 个有
- `MinimaxH3LatentUpscaler3D` —— 10/18 个有
- `SaveImage` —— 10/18 个有
- `SplitSigmas` —— 10/18 个有
- `VHS_LoadVideo` —— 10/18 个有
- `easy float` —— 10/18 个有
- `Text` —— 6/18 个有
- `Audio Duration (mtb)` —— 5/18 个有
- `AudioCrop` —— 5/18 个有
- `AudioSeparation` —— 5/18 个有
- `MathExpression|pysssss` —— 5/18 个有
- `SaveText` —— 5/18 个有
- `VRGDG_MiniMaxH3AudioDrive` —— 5/18 个有
- `Any Switch (rgthree)` —— 4/18 个有
- `Fast Groups Bypasser (rgthree)` —— 4/18 个有
- `PrimitiveBoolean` —— 4/18 个有
- `PrimitiveStringMultiline` —— 4/18 个有
- `PurgeVRAM_UTK` —— 4/18 个有
- `UniBlockSwap` —— 4/18 个有
- `VHS_LoadAudioUpload` —— 4/18 个有
- `easy ifElse` —— 4/18 个有
- `easy showAnything` —— 4/18 个有
- `H3SigmaRefiner` —— 3/18 个有
- `MuyeTextEditOutput` —— 1/18 个有
- `PreviewAny` —— 1/18 个有
- `easy cleanGpuUsed` —— 1/18 个有

## 典型参数

| 参数 | 中位数/常用 | 区间 | 样本 | 一致性 |
|---|---|---|---|---|
| 宽度 | 80 | 80 - 80 | 18 | 100% |
| 高度 | 80 | 80 - 80 | 18 | 100% |
| 采样步数 | 4 | 4 - 4 | 18 | 100% |
| Prompt 约束强度(CFG) | 4.5 | 4.5 - 4.5 | 18 | 100% |
| 采样算法 | er_sde | - | 18 | 100% |
| 调度器 | beta | - | 18 | 100% |
| 重绘幅度 | 1 | 1 - 1 | 18 | 100% |

## 常见问题

| 问题 | 出现次数 | 严重度 | 示例 |
|---|---|---|---|
| Steps较低可能导致细节不足 | 19/18 | medium | Steps较低，可能导致细节不足 → 建议增加到20-30 |

## 建议与风险

- 宽度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 高度 中位数 80，观测区间 80 - 80，18 个样本，取值集中（一致性 100%）
- 采样步数 中位数 4，观测区间 4 - 4，18 个样本，取值集中（一致性 100%）
- Prompt 约束强度(CFG) 中位数 4.5，观测区间 4.5 - 4.5，18 个样本，取值集中（一致性 100%）
- 采样算法 最常用 er_sde，18 个样本，一致性 100%
- 调度器 最常用 beta，18 个样本，一致性 100%
- 重绘幅度 中位数 1，观测区间 1 - 1，18 个样本，取值集中（一致性 100%）
- 高发问题（19/18 个样本）：Steps较低可能导致细节不足
