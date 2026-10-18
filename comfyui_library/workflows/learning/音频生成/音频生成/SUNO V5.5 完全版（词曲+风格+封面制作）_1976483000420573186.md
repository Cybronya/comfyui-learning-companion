---
key: 音频生成/音频生成/SUNO V5.5 完全版（词曲+风格+封面制作）_1976483000420573186.json
name: SUNO V5.5 完全版（词曲+风格+封面制作）_1976483000420573186
type: Unknown Workflow
status: completed
source: json
file: comfyui_library/workflows/音频生成/音频生成/SUNO V5.5 完全版（词曲+风格+封面制作）_1976483000420573186.json
hash: 5577ce0ab535b9a6
coverage: 0.518519
learned_at: 2026-10-18 01:46:52
nodes: [JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, JjkText, ImpactSwitch, RH_Suno_Lyrics, ShowText, ShellAgentPluginOutputText, JjkText, JjkText, easy ifElse, easy ifElse, PrimitiveBoolean, easy ifElse, ModelSamplingAuraFlow, CFGNorm, VAEDecode, LoraLoaderModelOnly, LoraLoaderModelOnly, NunchakuQwenImageDiTLoader, ShowText, ShellAgentPluginOutputText, ShowText, CLIPLoader, KSampler, Fast Groups Bypasser (rgthree), PrimitiveBoolean, JjkText, JjkText, TextCombinerTwo, easy showAnything, SaveImage, VAELoader, RH_LLMAPI_NODE, CR SDXL Aspect Ratio, JjkText, RH_RhartAudioSunoV55Custom, SaveAudio, CLIPTextEncode, RH_Suno_Custom, RH_RhartAudioSunoV55Single, easy showAnything, CLIPTextEncode, TextCombinerTwo, easy showAnything]
patterns: []
missing: []
parameters: {"cfg": 1, "denoise": 1, "sampler_name": "euler", "scheduler": "simple", "seed": 7, "steps": 10}
---

# 音频生成/音频生成/SUNO V5.5 完全版（词曲+风格+封面制作）_1976483000420573186.json

> 来源文件 `comfyui_library/workflows/音频生成/音频生成/SUNO V5.5 完全版（词曲+风格+封面制作）_1976483000420573186.json`

## 结构

**生成流程**：Model → Condition → Sampling → Decode → Output → Other

**节点**（54 个）：
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `JjkText`
- `ImpactSwitch`
- `RH_Suno_Lyrics`
- `ShowText`
- `ShellAgentPluginOutputText`
- `JjkText`
- `JjkText`
- `easy ifElse`
- `easy ifElse`
- `PrimitiveBoolean`
- `easy ifElse`
- `ModelSamplingAuraFlow`
- `CFGNorm`
- `VAEDecode` ★核心
- `LoraLoaderModelOnly` ★核心
- `LoraLoaderModelOnly` ★核心
- `NunchakuQwenImageDiTLoader`
- `ShowText`
- `ShellAgentPluginOutputText`
- `ShowText`
- `CLIPLoader`
- `KSampler` ★核心
- `Fast Groups Bypasser (rgthree)`
- `PrimitiveBoolean`
- `JjkText`
- `JjkText`
- `TextCombinerTwo`
- `easy showAnything`
- `SaveImage`
- `VAELoader`
- `RH_LLMAPI_NODE`
- `CR SDXL Aspect Ratio`
- `JjkText`
- `RH_RhartAudioSunoV55Custom`
- `SaveAudio`
- `CLIPTextEncode` ★核心
- `RH_Suno_Custom`
- `RH_RhartAudioSunoV55Single`
- `easy showAnything`
- `CLIPTextEncode` ★核心
- `TextCombinerTwo`
- `easy showAnything`

## 关键参数

- `seed` = `7`
- `steps` = `10`
- `cfg` = `1`
- `sampler_name` = `euler`
- `scheduler` = `simple`
- `denoise` = `1`

## 知识

覆盖率 **52%**（28/54）

**有卡**：`RH_Suno_Lyrics`、`ShowText`、`ShellAgentPluginOutputText`、`PrimitiveBoolean`、`ModelSamplingAuraFlow`、`CFGNorm`、`VAEDecode`、`LoraLoaderModelOnly`、`NunchakuQwenImageDiTLoader`、`CLIPLoader`、`KSampler`、`TextCombinerTwo`、`SaveImage`、`VAELoader`、`RH_LLMAPI_NODE`、`CR SDXL Aspect Ratio`、`RH_RhartAudioSunoV55Custom`、`SaveAudio`、`CLIPTextEncode`、`RH_Suno_Custom`、`RH_RhartAudioSunoV55Single`

**用到的条目**：KSampler、VAEDecode、VAELoader、LoraLoaderModelOnly、CLIPTextEncode、CLIPLoader、SaveImage、CFGNorm
