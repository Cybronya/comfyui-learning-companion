---
key: 视频生成/文生视频/速度超快的-LTXV-13b-0.9.7-dev-FP8版AI视频生成 + 高清放大+三提示词切换_1921116255519178753.json
name: 速度超快的-LTXV-13b-0.9.7-dev-FP8版AI视频生成 + 高清放大+三提示词切换_1921116255519178753
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/视频生成/文生视频/速度超快的-LTXV-13b-0.9.7-dev-FP8版AI视频生成 + 高清放大+三提示词切换_1921116255519178753.json
hash: f21d9648e8860446
coverage: 0.333333
learned_at: 2026-10-10 23:14:12
nodes: [LTXVFilmGrain, STGGuiderAdvanced, GetNode, GetNode, GetNode, GetNode, STGAdvancedPresets, Note, GetNode, LTXVLatentUpsampler, VRAM_Debug, easy clearCacheAll, GetNode, VRAM_Debug, SetNode, Note, VRAM_Debug, SetNode, SetNode, KSamplerSelect, Note, VAEDecodeTiled, Set VAE Decoder Noise, SetNode, SetNode, easy clearCacheAll, easy cleanGpuUsed, easy clearCacheAll, easy cleanGpuUsed, LTXVTiledSampler, ImageResizeKJ, GetNode, GetNode, easy clearCacheAll, GetNode, Note, VAEDecodeTiled, GetNode, easy cleanGpuUsed, easy clearCacheAll, GetNode, GetNode, RandomNoise, easy cleanGpuUsed, easy clearCacheAll, SetNode, GetNode, Note, LTXVConditioning, SetNode, SetNode, SetNode, LTXVBaseSampler, CLIPLoader, SetNode, Fast Groups Muter (rgthree), GetNode, VHS_VideoCombine, GetNode, GetNode, STGGuiderAdvanced, easy clearCacheAll, GetNode, GetNode, STGAdvancedPresets, CheckpointLoaderSimple, easy showAnything, GetNode, Note, GetNode, GetNode, RandomNoise, GetNode, CLIPTextEncode, CLIPTextEncode, LTXVPromptEnhancer, LTXVPromptEnhancerLoader, GetNode, RH_Translator, RH_Captioner, Note, GetNode, SetNode, DisplayText_Zho, RH_Translator, DisplayText_Zho, DisplayText_Zho, LTXVLatentUpsamplerModelLoader, GetNode, Note, LayerUtility: ImageScaleByAspectRatio V2, SetNode, SetNode, SetNode, SetNode, Primitive integer [Crystools], SetNode, GetNode, GetNode, SetNode, LTXVAdainLatent, CR Text, CR Text Input Switch (4 way), Note, Note, Note, BasicScheduler, SplitSigmas, LoadImage, CR Text, VHS_VideoCombine]
patterns: []
missing: [CR Text, CR Text, CR Text Input Switch (4 way), LayerUtility: ImageScaleByAspectRatio V2, Primitive integer [Crystools], easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy cleanGpuUsed, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, easy clearCacheAll, Set VAE Decoder Noise]
parameters: {"checkpoint": "ltxv-13b-0.9.7-dev_fp8_e4m3fn.safetensors"}
discoveries: [次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text` 知识库中没有该节点类型的任何知识, 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识, 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识, 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识, 次要节点 `Set VAE Decoder Noise` 仅有 VAE 的通用知识，没有该节点自己的说明]
---

# 视频生成/文生视频/速度超快的-LTXV-13b-0.9.7-dev-FP8版AI视频生成 + 高清放大+三提示词切换_1921116255519178753.json

> 来源文件 `comfyui_library/workflows/视频生成/文生视频/速度超快的-LTXV-13b-0.9.7-dev-FP8版AI视频生成 + 高清放大+三提示词切换_1921116255519178753.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Process → Other

**节点**（111 个）：
- `LTXVFilmGrain`
- `STGGuiderAdvanced`
- `GetNode`
- `GetNode`
- `GetNode`
- `GetNode`
- `STGAdvancedPresets`
- `Note`
- `GetNode`
- `LTXVLatentUpsampler` ★核心
- `VRAM_Debug`
- `easy clearCacheAll`
- `GetNode`
- `VRAM_Debug`
- `SetNode`
- `Note`
- `VRAM_Debug`
- `SetNode`
- `SetNode`
- `KSamplerSelect` ★核心
- `Note`
- `VAEDecodeTiled` ★核心
- `Set VAE Decoder Noise`
- `SetNode`
- `SetNode`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `easy cleanGpuUsed`
- `LTXVTiledSampler` ★核心
- `ImageResizeKJ`
- `GetNode`
- `GetNode`
- `easy clearCacheAll`
- `GetNode`
- `Note`
- `VAEDecodeTiled` ★核心
- `GetNode`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `easy cleanGpuUsed`
- `easy clearCacheAll`
- `SetNode`
- `GetNode`
- `Note`
- `LTXVConditioning`
- `SetNode`
- `SetNode`
- `SetNode`
- `LTXVBaseSampler` ★核心
- `CLIPLoader`
- `SetNode`
- `Fast Groups Muter (rgthree)`
- `GetNode`
- `VHS_VideoCombine`
- `GetNode`
- `GetNode`
- `STGGuiderAdvanced`
- `easy clearCacheAll`
- `GetNode`
- `GetNode`
- `STGAdvancedPresets`
- `CheckpointLoaderSimple` ★核心
- `easy showAnything`
- `GetNode`
- `Note`
- `GetNode`
- `GetNode`
- `RandomNoise`
- `GetNode`
- `CLIPTextEncode` ★核心
- `CLIPTextEncode` ★核心
- `LTXVPromptEnhancer`
- `LTXVPromptEnhancerLoader`
- `GetNode`
- `RH_Translator`
- `RH_Captioner`
- `Note`
- `GetNode`
- `SetNode`
- `DisplayText_Zho`
- `RH_Translator`
- `DisplayText_Zho`
- `DisplayText_Zho`
- `LTXVLatentUpsamplerModelLoader` ★核心
- `GetNode`
- `Note`
- `LayerUtility: ImageScaleByAspectRatio V2`
- `SetNode`
- `SetNode`
- `SetNode`
- `SetNode`
- `Primitive integer [Crystools]`
- `SetNode`
- `GetNode`
- `GetNode`
- `SetNode`
- `LTXVAdainLatent`
- `CR Text`
- `CR Text Input Switch (4 way)`
- `Note`
- `Note`
- `Note`
- `BasicScheduler`
- `SplitSigmas`
- `LoadImage`
- `CR Text`
- `VHS_VideoCombine`

## 关键参数

- `checkpoint` = `ltxv-13b-0.9.7-dev_fp8_e4m3fn.safetensors`

## 知识

覆盖率 **33%**（37/111）

**有卡**：`LTXVFilmGrain`、`STGGuiderAdvanced`、`STGAdvancedPresets`、`LTXVLatentUpsampler`、`VRAM_Debug`、`KSamplerSelect`、`VAEDecodeTiled`、`LTXVTiledSampler`、`ImageResizeKJ`、`RandomNoise`、`LTXVConditioning`、`LTXVBaseSampler`、`CLIPLoader`、`VHS_VideoCombine`、`CheckpointLoaderSimple`、`CLIPTextEncode`、`LTXVPromptEnhancer`、`LTXVPromptEnhancerLoader`、`RH_Translator`、`RH_Captioner`、`DisplayText_Zho`、`LTXVLatentUpsamplerModelLoader`、`LTXVAdainLatent`、`BasicScheduler`、`SplitSigmas`、`LoadImage`

**缺卡**（17）：`CR Text`、`CR Text`、`CR Text Input Switch (4 way)`、`LayerUtility: ImageScaleByAspectRatio V2`、`Primitive integer [Crystools]`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy cleanGpuUsed`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`easy clearCacheAll`、`Set VAE Decoder Noise`

**用到的条目**：CheckpointLoaderSimple、CLIPTextEncode、CLIPLoader、LoadImage、KSamplerSelect、LTXVLatentUpsampler、LTXVBaseSampler、LTXVLatentUpsamplerModelLoader

## 学习发现

- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text` 知识库中没有该节点类型的任何知识
- 次要节点 `CR Text Input Switch (4 way)` 知识库中没有该节点类型的任何知识
- 次要节点 `LayerUtility: ImageScaleByAspectRatio V2` 知识库中没有该节点类型的任何知识
- 次要节点 `Primitive integer [Crystools]` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy cleanGpuUsed` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `easy clearCacheAll` 知识库中没有该节点类型的任何知识
- 次要节点 `Set VAE Decoder Noise` 仅有 VAE 的通用知识，没有该节点自己的说明
